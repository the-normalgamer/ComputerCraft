

function github_read_file(username, repository_name, file_path)
    local headers = {}
    url = "https://raw.githubusercontent.com/"..username.."/"..repository_name.."/master/".. file_path
    r = http.get(url, headers)
    return r
end

