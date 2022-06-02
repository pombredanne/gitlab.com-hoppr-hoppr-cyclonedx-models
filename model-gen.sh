curl -L -o cyclonedx_dwnld.tar.gz https://github.com/CycloneDX/specification/archive/refs/tags/1.4.tar.gz -vvv
tar -xvf cyclonedx_dwnld.tar.gz

#mkdir cyclonedx_types
read -p "Which version of CycloneDX would you like to make a pydantic model of?(Answer with _._ format - EX: 1.4): " answer

if [[ $answer =~ "1.4" ]]; then
    datamodel-codegen  --input ./specification-1.4/schema/bom-1.4.schema.json --input-file-type jsonschema --output ./pydantic1_4
    sed -i s/unique_items=True/"'REMOVED LM unique_items=True'"/g ./pydantic1_4/__init__.py
elif [[ $answer =~ "1.3" ]]; then
    datamodel-codegen  --input ./specification-1.4/schema/bom-1.3.schema.json --input-file-type jsonschema --output ./pydantic1_3
    sed -i s/unique_items=True/"'REMOVED LM unique_items=True'"/g ./pydantic1_3/__init__.py
elif [[ $answer =~ "1.2" ]]; then
    datamodel-codegen  --input ./specification-1.4/schema/bom-1.2.schema.json --input-file-type jsonschema --output ./pydantic1_2
    sed -i s/unique_items=True/"'REMOVED LM unique_items=True'"/g ./pydantic1_2/__init__.py
else
    echo "That is not a current version."
fi


