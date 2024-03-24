# employ puppet to make changes to the default ssh config fle
# to ensure no one connects to a server without typing a password.

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# Regex match explanation
#
# ^       start of the line
# [#]*  atleast one hash char
# [\s]*  zero or more white space chars
# (?i)IdentityFile case insensitive "IdentityFile"
# [\s]+ at least one whitespace char
# ~/.ssh/id_rsa The ssh private key file path we want to replace
# $      end of the line

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}

# Regex match explanation
#
# ^       beginning of the line
# [#]*  atleast one hash char
# [\s]*  zero or more white space char
# (?i)PasswordAuthentication case insensitive "PasswordAuthentication"
# [\s]+ at least one whitespace char
# (yes|no) with the value "yes" or the value "no"
# $      end of the line
