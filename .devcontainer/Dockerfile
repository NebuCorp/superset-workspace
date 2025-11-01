FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
################################################################################################
#      For Ubuntu 22.04, you should use "apt" instead of "apt-get"                             #
#      when running on dockerfile though use apt-get for non-interactive                       #
#      as it is the recommended package manager and considered the more modern choice          #
#      https://www.tecmint.com/ubuntu-22-04-release-notes/                                     #
################################################################################################

# Update and install base dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    jq \
    git \
    vim \
    build-essential \
    python3 \
    python3.10-venv \
    python3-pip \
    software-properties-common \
    unzip \
    zip \
    && rm -rf /var/lib/apt/lists/*


# Install Postgres Client
# https://www.postgresql.org/download/linux/ubuntu/
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg && \
    apt-get update && apt-get install -y locales postgresql-client-17

# Variables required by psql
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

#Install fonts for zsh
RUN apt-get update && apt-get install -y \
    fonts-powerline \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI v2
# https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip - use for arm64 (mac Silicon)
# https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip - use for x86_64 (windows, intel)

# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" \
#     && unzip awscliv2.zip \
#     && ./aws/install \
#     && rm -rf awscliv2.zip aws/

# Install zsh and set it as default shell
RUN apt-get update && apt-get install -y zsh \
    && chsh -s $(which zsh)


# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Optional: Install popular Oh My Zsh plugins
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions \
    && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

COPY .devcontainer/.zshrc /root/.zshrc



WORKDIR /workspace

# Add permissions handling
RUN mkdir -p /root/.vscode-server/data/Machine \
    && chmod -R 777 /root/.vscode-server

EXPOSE 3000