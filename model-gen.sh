#!/bin/bash
answer=$1
cd=cyclonedx_dwnld.tar.gz

HTTP_CODE=$(curl -s -w "%{http_code}\n" -o /dev/null https://github.com/CycloneDX/specification/releases/tag/$answer)

if [ $HTTP_CODE != "404" ]; then
    curl -L -o $cd https://github.com/CycloneDX/specification/archive/refs/tags/$answer.tar.gz 
    tar -xvf $cd
    rm $cd

    py_file=cyclonedx_$answer
    py_file=${py_file//./_} 

    poetry run datamodel-codegen --input ./specification-$answer/schema/bom-$answer.schema.json --input-file-type jsonschema --output ./hoppr_cyclonedx_models/$py_file
    sed -i s/unique_items=True\)/") unique_items=True"/g ./hoppr_cyclonedx_models/$py_file/__init__.py
    sed -i s/unique_items=True\,/"unique_items=True"/g ./hoppr_cyclonedx_models/$py_file/__init__.py
    sed -i s/unique_items=True/""/g ./hoppr_cyclonedx_models/$py_file/__init__.py
    #sed -i s/unique_items=True\)/") unique_items=True"/g ./hoppr_cyclonedx_models/$py_file/__init__.py
    #sed -i s/unique_items=True/"# REMOVED LM unique_items=True"/g ./hoppr_cyclonedx_models/$py_file/__init__.py
else 
    echo "The version selected does not exist. Example Usage: ./model-gen.sh 1.4"
fi



