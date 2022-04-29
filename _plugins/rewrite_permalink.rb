# Custom plugin to add author username to permalinks of posts

module Jekyll
  class RewritePermalinks < Generator
      safe true
      priority :low

      def generate(site)
        Jekyll.logger.info "RewritePermalinks:", "Rewriting permalinks..."

        count = 0

        site.posts.docs.each do |item|
            # Only process posts that were added after 28 April and have no permalink set
            if item.data['date'] > Time.parse('28 April 2022') && item.data['permalink'].nil?
                item.data['permalink'] = item.data['author'] + '/' + Utils.slugify(item.data['slug'])

                count += 1
            end
        end

        Jekyll.logger.info "RewritePermalinks:", "Rewrote permalink for #{count} posts."
      end
  end
end