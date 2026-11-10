FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    procps \
    && rm -rf /var/lib/apt/lists/*

# A background process holds the flag in its environment
# Players must find the process and read /proc/<pid>/environ
RUN echo '#!/bin/bash
export XITA_NURTURE="ISHTAR{UR_y34rns_thr0ugh_hungr3}"
export DECOY_1="not_the_flag"
export DECOY_2="keep_looking"
# The worm does not sleep. It waits.
while true; do sleep 3600; done
' > /usr/local/bin/ur-daemon && chmod +x /usr/local/bin/ur-daemon

# Autostart via profile
RUN echo '/usr/local/bin/ur-daemon &' >> /etc/profile && \
    echo 'disown' >> /etc/profile

# MOTD hint
RUN echo '===============================================' > /etc/motd && \
    echo '        RESONANT FURY // HELM INTERFACE' >> /etc/motd && \
    echo '===============================================' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo ' Ur yearns for nurture. It does so through hunger.' >> /etc/motd && \
    echo ' Something runs in the deep. It will not be controlled.' >> /etc/motd && \
    echo ' Find the wrath that refuses to be manipulated.' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo '===============================================' >> /etc/motd

CMD ["bash", "--login"]
