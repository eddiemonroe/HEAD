#!/usr/bin/env bash
#
# To enable the completions either:
#  - place this file in /etc/bash_completion.d
#  or
#  - copy this file to e.g. ~/.hr/hr-completion.sh and add the line
#    below to your .bashrc after bash completion features are loaded
#    . ~/.hr/hr-completion.sh

_hr() {
  local command
  local hr_commands="init get install uninstall build clean cmd env update normal_opencog dev_opencog run stop"
  local cur=${COMP_WORDS[COMP_CWORD]}
  local words=${COMP_WORDS[@]}
  local cword=$COMP_CWORD

  _init_completion || return

  for (( i=1 ; i < ${cword} ; i++ )) ; do
    if [[ ${words[i]} == -* ]] ; then continue; fi
    if [[ ${hr_commands} == *${words[i]}* ]] ; then
      command=${words[i]}
    fi
  done

  case ${command} in
    install|uninstall|build|get|clean|update)
      local args=$(hr cmd list_components ${command} 2> /dev/null)
      COMPREPLY=($(compgen -W "${args}" -- ${cur}))
      ;;
    run)
      if (( ${cword} == 2 )); then
        local args=$(hr cmd list_robots 2> /dev/null)
        COMPREPLY=($(compgen -W "${args}" -- ${cur}))
      fi
      ;;
    *)
      if (( ${cword} >= 2 )); then
        COMPREPLY=()
      else
        COMPREPLY=($(compgen -W "${hr_commands}" -- ${cur}))
      fi
      ;;
  esac
}

complete -F _hr hr
