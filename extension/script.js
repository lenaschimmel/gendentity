chrome.storage.sync.get({
    possessivePronoun: 'her',
	    }, function(items) {
	window.possessivePronoun = items.possessivePronoun;
	walk(document.body);
    });
	
function walk(node)
{
    pnodes = node.getElementsByTagName('p');
    console.log(pnodes);
    for (i in pnodes) {
	pnodes[i].textContent = replaceAll(pnodes[i].textContent);
    }
    return node;
}

function replaceAll(text)
{
    var after = possessivePronoun;

    text = text.split(/[ ]+his/i).join(" "+after);

    return text;
}