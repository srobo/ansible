Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 4
  end

  # Required so that apt cache is populated before ansible runs
  config.vm.provision "shell", privileged: true, inline: "apt-get update && apt-get upgrade -y"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.compatibility_mode = "2.0"
    ansible.become = true  # Run ansible as root

    ansible.groups = {
      "web-proxies" => ["sr-proxy"],
    }
  end

  # This name is what's looked up in the Ansible host_vars.
  config.vm.define "sr-proxy" do |web|
    web.vm.box = "ubuntu/focal64"

    web.vm.network "private_network", ip: "192.168.56.56"
    web.vm.hostname = "sr-proxy.local"
  end
end
