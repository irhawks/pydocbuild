function dt() {
    local shortcut=${1:-list}
    local helpopt=$2

    if test "$shortcut" = "help"
    then
        shortcut=$helpopt
        helpopt="--help"
    fi

    local expr_rx=$(echo $shortcut | sed 's/\(.\)/\1[^_]*_/g')

    declare -A seen
    shift
    doit list | while read papabile helpdoc
    do
        case $shortcut in
            list)
                local alias=$(echo $papabile | sed 's/\(.\)[^_]*_*/\1/g')
                if test -z "${seen[$alias]}"
                then
                    echo -e "$alias, $papabile\n\t$helpdoc\n"
                    seen[$alias]=t
                fi
                ;;
            *)
                if test "$papabile" = "$shortcut" -o $(expr "$papabile" : "$expr_rx*") -gt 0
                then
                    if test "$helpopt" = "-h" -o "$helpopt" = "--help"
                    then
                        doit help $papabile
                    else
                        doit $papabile $*
                    fi
                    seen[$papabile]=t
                    break
                fi
                ;;
        esac
    done
}
complete -F dt doit
