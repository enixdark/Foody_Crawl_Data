#!/bin/bash



echo "========== processing virtual env ====================="
virtualenv pyfoody

echo "active virtual env"
source pyfoody/bin/activate
echo "install lib/module python for project"
pip install requements.txt
echo "========== completed =================================="



echo "to start crawl data please run `scrapy crawl foody`"
echo ""
echo "before starting the program, please setup mongo database and setting it in files settings of project"
echo ""
