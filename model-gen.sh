#!/bin/bash
answer=$1

HTTP_CODE=$(curl -s -w "%{http_code}\n" -o /dev/null https://github.com/CycloneDX/specification/releases/tag/$answer -vvv)

if [ $HTTP_CODE != "404" ]; then
    curl -L -o cyclonedx_dwnld.tar.gz https://github.com/CycloneDX/specification/archive/refs/tags/$answer.tar.gz -vvv
    tar -xvf cyclonedx_dwnld.tar.gz 

    py_file=pydantic$answer
    py_file=${py_file//./_} 

    datamodel-codegen  --input ./specification-$answer/schema/bom-$answer.schema.json --input-file-type jsonschema --output ./$py_file
    sed -i s/unique_items=True/"'REMOVED LM unique_items=True'"/g ./$py_file/__init__.py
else 
    echo "The version selected does not exist."
fi



