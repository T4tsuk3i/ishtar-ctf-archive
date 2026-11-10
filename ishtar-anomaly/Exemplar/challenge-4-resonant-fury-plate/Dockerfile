FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    cron \
    && rm -rf /var/lib/apt/lists/*

# The Witness whispers on a schedule. The flag is in cron.
# Players must find and read the crontab or cron.d files.
RUN echo '# The whisper comes at midnight' > /etc/cron.d/witness-whisper && \
    echo '# Young Sathona. The end is coming. A great cataclysm.' >> /etc/cron.d/witness-whisper && \
    echo '# Salvation lies in the Deep.' >> /etc/cron.d/witness-whisper && \
    echo '' >> /etc/cron.d/witness-whisper && \
    echo '0 0 * * * root echo "ISHTAR{x0l_wh15p3r5_fr0m_th3_d33p}" >> /dev/null' >> /etc/cron.d/witness-whisper && \
    chmod 0644 /etc/cron.d/witness-whisper

# Decoy cron jobs to add noise
RUN echo '# System maintenance' > /etc/cron.d/osmium-maintenance && \
    echo '*/5 * * * * root /bin/true' >> /etc/cron.d/osmium-maintenance && \
    echo '30 3 * * * root /bin/false' >> /etc/cron.d/osmium-maintenance && \
    chmod 0644 /etc/cron.d/osmium-maintenance

RUN echo '# Moon tracking daemon' > /etc/cron.d/silver-moon && \
    echo '15 * * * * root /bin/echo "moon phase nominal"' >> /etc/cron.d/silver-moon && \
    chmod 0644 /etc/cron.d/silver-moon

RUN echo '===============================================' > /etc/motd && \
    echo '       RESONANT FURY // PLATE INTERFACE' >> /etc/motd && \
    echo '===============================================' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo ' Xol yearned for nurture. It did so amongst the thousands.' >> /etc/motd && \
    echo ' The Witness whispers. The whispers are scheduled.' >> /etc/motd && \
    echo ' Brave minds. Clever minds. Listen at the right time.' >> /etc/motd && \
    echo '' >> /etc/motd && \
    echo '===============================================' >> /etc/motd

CMD ["bash", "--login"]
