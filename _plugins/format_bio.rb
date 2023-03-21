require 'date'
require 'liquid'

module Jekyll
  module FormatBio
    def format_bio(author)
      return author['bio'] if author['birthdate'].nil?

      today = Date.today
      since = Date.parse(author['birthdate'])
      years = today.year - since.year

      if (today.month < since.month) || (today.month == since.month && today.day < since.day)
       years -= 1
      end

      return author['bio'].gsub('{ age }', years.to_s)
    end
  end
end

Liquid::Template.register_filter(Jekyll::FormatBio)
