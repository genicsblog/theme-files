# Custom jekyll plugin to mark text segments on articles with audio

require "json"
require "dotenv"
require "jekyll"
require "nokogiri"
require "net/http"

module Jekyll
  module MarkSegments

    def env
      Dotenv.load

      {
        "project_id" => ENV["BEYONDWORDS_PROJECT_ID"],
        "api_key" => ENV["BEYONDWORDS_API_KEY"]
      }
    end

    def cache
      @@cache ||= Jekyll::Cache.new("SegmentsCache")
    end

    def get_segments(content_id)
      cache.getset(content_id) do
        url = URI(
          "https://api.beyondwords.io/v1/projects/#{env['project_id']}/content/#{content_id}?segments=full"
        )

        http = Net::HTTP.new(url.host, url.port)
        http.use_ssl = true

        request = Net::HTTP::Get.new(url)
        request["accept"] = "application/json"
        request["X-Api-Key"] = env["api_key"]

        response = http.request(request)
        response.read_body
      end
    end

    def mark_segments(html, content_id)
      if content_id.class == Integer and content_id == 4052597
        doc = Nokogiri::HTML.fragment(html)
        return html unless doc

        json = JSON.parse(get_segments(content_id))
        segments = json['segments']

        counter = 1
        
        for element in doc.css('*') do
          if (
            !is_first_child_img(element) and
            element.get_attribute("data-marker") != "none" and
            ['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'].include?(element.name)
          )
            begin
              element.set_attribute('data-beyondwords-marker', segments[counter]['marker'])
              counter += 1
            rescue
              break
            end
          end
        end
        
        doc.to_s
      end
    end

    def is_first_child_img(element)
      if (
        !element.element_children.nil? and
        element.element_children[0].class == Nokogiri::XML::Element and
        element.element_children[0].name == "img"
      )
        return true
      end

      return false
    end

  end
end

Liquid::Template.register_filter(Jekyll::MarkSegments)
