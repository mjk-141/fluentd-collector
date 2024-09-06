FROM fluent/fluentd:v1.16.2-debian-1.1
USER root
RUN buildDeps="sudo make gcc g++ libc-dev" \
 && apt-get update \
 && apt-get install -y --no-install-recommends $buildDeps \
 && sudo apt-get install -y libmariadb-dev \
 && sudo gem install fluent-plugin-opensearch \
 && sudo gem install fluent-plugin-out-http -v 0.1.4 \
 && sudo gem install fluent-plugin-mysql-bulk \
 && sudo gem sources --clear-all \
 && SUDO_FORCE_REMOVE=yes \
    apt-get purge -y --auto-remove \
    -o APT::AutoRemove::RecommendsImportant=false \
    $buildDeps \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem
