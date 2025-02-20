

function github_read_file(username, repository_name, file_path, github_token)
    local headers = {}
    headers['Authorization'] = "token "+github_token
    url = "https://api.github.com/repos/" + username + "/" + repository_name + "/contents/"+file_path
    r = http.get(url, headers)
    return r
end

print()