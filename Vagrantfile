Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.network "private_network", ip: "192.168.42.42"
  config.vm.hostname = "sr-vm.local"

  # Required so that apt cache is populated before ansible runs
  config.vm.provision "shell", privileged: true, inline: "apt-get update && apt-get upgrade -y"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.compatibility_mode = "2.0"
    ansible.become = true  # Run ansible as root
  end
end
