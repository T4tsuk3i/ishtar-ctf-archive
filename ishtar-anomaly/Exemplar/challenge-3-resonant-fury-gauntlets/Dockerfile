FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    attr \
    file \
    stat \
    && rm -rf /var/lib/apt/lists/*

# The flag is encoded into extended file attributes of the leviathan's rib
# Yul is honest - the data IS there. Players just need to look at it properly.
RUN mkdir -p /var/lib/leviathan && \
    echo "A rib many times larger than the Subjugator himself." > /var/lib/leviathan/rib.txt && \
    setfattr -n user.resonance -v "ISHTAR{y4l_5p34k5_thr0ugh_h0n35ty}" /var/lib/leviathan/rib.txt && \
    setfattr -n user.origin -v "Torn from the chest of the cruel Leviathan" /var/lib/leviathan/rib.txt && \
    setfattr -n user.wielder -v "Rhulk, Disciple of the Witness" /var/lib/leviathan/rib.txt

# Scatter decoy files
RUN for name in bone claw scale spine fang; do \
      echo "Not what you seek." > /var/lib/leviathan/$name.relic; \
    done

RUN echo '===============================================' > /etc/motd && \
    echo '      RESONANT FURY // GAUNTLETS INTERFACE' >> /etc/motd && \
    echo '===============================================' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo ' Yul yearns for nurture. It does so through honesty.' >> /etc/motd && \
    echo ' The rib dropped into the Deep. What does it carry?' >> /etc/motd && \
    echo ' Turn back from the world-killing way — or look closer.' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo '===============================================' >> /etc/motd

CMD ["bash", "--login"]
