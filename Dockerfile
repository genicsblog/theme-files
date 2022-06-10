FROM timbru31/ruby-node:2.7
ENV JEKYLL_ENV=dev
WORKDIR /app
COPY Gemfile ./
COPY package.json ./
RUN gem install jekyll bundler
RUN npm install
RUN bundle install
RUN git clone https://github.com/genicsblog/genicsblog.com genicsblog
RUN mv genicsblog/* .
RUN rm -rf genicsblog
COPY . .
EXPOSE 4000
CMD [ "bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0" ]