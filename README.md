# Googd0rk
## 2023 Rewrite
googd0rk is a tool for firing off google dorks against a target domain, it is purely for OSINT against a specific target domain. 

I [initially wrote a version of this tool a while back](https://github.com/ZephrFish/GoogD0rker) but have since rewritten it to be a bit more efficient and allow for threading etc. There are certainly other tools out there that do similar and more but I just like creating things.

This will output all the google results for each of the tasks so you can hopefully find a vunerability. A 503 error means you need a new IP as google knows you're up to something!  This will output the results to files and then you can browse and see what you have found.

### Setup
The only pre-requisites are python3-requests which can be installed via requirements:

`pip3 install -r requirements.txt`

### Example Usage:
To execute the script against the domain blog.zsec.uk, you would run the following command:
```
python googd0rk.py blog.zsec.uk
```

This will run the script with the default output file d0rklog.log, default query file dork_queries.txt, and default user agent file useragents.txt, using 5 threads.

If you want to specify a different output file, query file, or user agent file, you can use the -o, -q, and -u arguments, respectively. For example, to use a query file called `custom_queries.txt` and an output file called custom_output.log, you can run the following command:

```
python googd0rk.py blog.zsec.uk -o custom_output.log -q custom_queries.txt
```

To specify the maximum number of parallel threads, you can use the -t argument. For example, to use 8 threads, you can run the following command:

```
python googd0rk.py blog.zsec.uk -t 8
```

### Todo
- Implement AWS API Gateway to rotate IP per request to save throttling.