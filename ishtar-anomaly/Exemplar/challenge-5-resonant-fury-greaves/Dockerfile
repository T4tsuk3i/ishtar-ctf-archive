FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    iproute2 \
    && rm -rf /var/lib/apt/lists/*

# Akka keeps secrets. The flag is served over a local socket listener.
# Players must discover the listening port and connect to retrieve the secret.
RUN echo '#!/bin/bash
# The Subjugator knew of our strengths. Our power to grip the mind.
# He kept us. For this.
FLAG="ISHTAR{4kk4_k33p5_thr0ugh_53cr3t5}"

while true; do
    echo -e "Segment returned to Fundament.\nThe current carries it to the shores.\n${FLAG}" | nc -l -p 9447 -q 1 2>/dev/null
done
' > /usr/local/bin/akka-daemon && chmod +x /usr/local/bin/akka-daemon

RUN echo '/usr/local/bin/akka-daemon &' >> /etc/profile && \
    echo 'disown' >> /etc/profile

# Misleading open files in /var to throw off naive searches
RUN mkdir -p /var/lib/fundament && \
    for i in segment_1 segment_2 segment_3 larvae_cache; do \
      echo "Not what you seek. The deep does not yield easily." > /var/lib/fundament/$i; \
    done

RUN echo '===============================================' > /etc/motd && \
    echo '      RESONANT FURY // GREAVES INTERFACE' >> /etc/motd && \
    echo '===============================================' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo ' Akka yearned for nurture. It did so through secrets.' >> /etc/motd && \
    echo ' He knew of our strengths. Our power to grip and guide.' >> /etc/motd && \
    echo ' Living pieces, set adrift. Find where the current leads.' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo '===============================================' >> /etc/motd

CMD ["bash", "--login"]
