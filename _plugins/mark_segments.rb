# Custom jekyll plugin to mark text segments on articles with audio

require "json"
require "dotenv"
require "jekyll"
require "nokogiri"
require "net/http"

module Jekyll
  module MarkSegments

    $counter = 0

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
        return response.read_body
      end
    end

    def set_segment(element, segments)
      if (
        !first_child_validation(element, "img") and
        element.get_attribute("data-marker") != "none" and
        element.get_attribute("data-beyondwords-marker").nil? and
        ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6"].include?(element.name)
      )
        begin
          # hack for li element with multiple children
          if element.name != "li" or (element.name == "li" and !first_child_validation(element, "p"))
            $counter += 1
            element.set_attribute("data-beyondwords-marker", segments[$counter]["marker"])
          end
        rescue
          $counter -= 1
        end

        for child in element.element_children
          set_segment(child, segments)
        end
      end
    end

    def mark_segments(html, content_id)
      return html if ENV['JEKYLL_ENV'] != 'production'

      doc = Nokogiri::HTML.fragment(html)
      return html unless doc

      if content_id.class == Integer
        json = JSON.parse(get_segments(content_id))
        segments = json["segments"]

        for element in doc.css("*") do
          set_segment(element, segments)
        end
      end

      $counter = 0
      doc.to_s
    end

    def first_child_validation(element, to_check)
      if (
        !element.element_children.nil? and
        element.element_children[0].class == Nokogiri::XML::Element and
        element.element_children[0].name == to_check
      )
        return true
      end

      return false
    end

  end
end

Liquid::Template.register_filter(Jekyll::MarkSegments)
