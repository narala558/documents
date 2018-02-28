for file in *
do
    mime=$(file --brief --mime-type "$file")

    case "$mime" in
    "image/jpeg")
        extension="jpeg"
        ;;
    "text/plain")
        extension="txt"
        ;;
    "application/pdf")
        extension="pdf"
        ;;
    *)
        continue;
        ;;
    esac

    filename="${file%.*}"

    mv "$file" "$filename.$extension"
done
