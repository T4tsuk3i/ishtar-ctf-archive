FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    findutils \
    && rm -rf /var/lib/apt/lists/*

# Eir yearns through ORDER. The flag is split into ordered fragments.
# Each fragment is in a different location. Players must find all pieces
# and assemble them in the correct numeric order.

# Full flag: ISHTAR{31r_nuRtur35_thr0ugh_0rd3r}
# Split: ISHTAR{ | 31r_nu | Rtur35_ | thr0ugh_ | 0rd3r}

RUN mkdir -p /var/lib/eir/throne && \
    # Fragment 0 — obvious location
    echo "Fragment [0/4]: ISHTAR{" > /var/lib/eir/throne/fragment_zero.txt && \
    \
    # Fragment 1 — buried in syslog-style location
    mkdir -p /var/log/upended && \
    echo "Fragment [1/4]: 31r_nu" > /var/log/upended/.vessel && \
    \
    # Fragment 2 — hidden in /opt
    mkdir -p /opt/savathun/throne_world && \
    echo "Fragment [2/4]: Rtur35_" > /opt/savathun/throne_world/.jealousy && \
    \
    # Fragment 3 — inside /tmp with a misleading name
    echo "Fragment [3/4]: thr0ugh_" > /tmp/not_the_flag.txt && \
    \
    # Fragment 4 — in /root home
    mkdir -p /root/.eir && \
    echo "Fragment [4/4]: 0rd3r}" > /root/.eir/price && \
    \
    # Decoy fragments with wrong ordering
    echo "DECOY: servitude" > /var/lib/eir/throne/decoy_a.txt && \
    echo "DECOY: survival" > /var/lib/eir/throne/decoy_b.txt && \
    echo "DECOY: ascendance" > /opt/savathun/decoy_hive.txt

RUN echo '===============================================' > /etc/motd && \
    echo '        RESONANT FURY // MARK INTERFACE' >> /etc/motd && \
    echo '===============================================' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo ' Eir yearns for nurture. It does so through order.' >> /etc/motd && \
    echo ' In the Deep. In ascendance. In the dark.' >> /etc/motd && \
    echo ' A price is paid in servitude. Collect what remains.' >> /etc/motd && \
    echo ' It must not be in vain.' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo '===============================================' >> /etc/motd

CMD ["bash", "--login"]
