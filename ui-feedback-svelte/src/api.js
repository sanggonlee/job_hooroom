const apiUrl = __app.env.API_URL;

export async function getPostings(params = {}) {
    const urlParams = Object.keys(params)
        .map(key => `${key}=${params[key]}`)
        .join('&');
    const url = `${apiUrl}/postings?${urlParams}`;
    const rawResp = await fetch(url);
    return await rawResp.json();
}

export async function trainWords(id, words) {
    const url = `${apiUrl}/train/${id}`;
    const rawResp = await fetch(url, { words });
    return await rawResp.json();
}
