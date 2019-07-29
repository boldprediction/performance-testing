import requests
import json
import datetime
import time

# strs = {'colorless', 'white', 'ivory', 'yellow', 'gold', 'olive', 'green', 'turquoise', 'azure', 'pink', 'crimson', 'maroon', 'lavender', 'purple', 'silver', 'brown', 'black', 'mottled', 'red', 'ruby', 'blue', 'spotted', 'round', 'oval', 'triangular', 'rectangular', 'square', 'shapeless', 'immense', 'massive', 'large', 'tiny', 'small', 'tall', 'short', 'wide', 'long', 'narrow', 'lean', 'round', 'flat', 'curved', 'wavy', 'ruffled', 'angular', 'hollow', 'tapered', 'wiry', 'lopsided', 'freckled', 'wrinkled', 'striped', 'bright', 'clear', 'glossy', 'jeweled', 'fiery', 'shimmering', 'muddy', 'drab', 'dark', 'grimy', 'worn', 'cluttered', 'fresh', 'flowery', 'transparent', 'sheer', 'opaque', 'muscular', 'handsome', 'robust', 'fragile', 'pale', 'perky', 'lacy', 'shadowy'}
strs = {'Bombay', 'New Delhi', 'Calcutta', 'Madras', 'Bangalore'}
reqlog = open("requests.log", "a+")
contrastlog = open("contrastlogs.log", "a+")


def sendRequest1(permutedstr):
    print(permutedstr)


def sendRequest(permutedstr):
    # str1 = 'colorless, white, ivory1, yellow, gold, olive, green, turquoise, azure, pink, crimson, maroon, lavender, purple, silver, brown, black, mottled, red, ruby, blue, spotted, round, oval, triangular, rectangular, square, shapeless, immense, massive, large, tiny, small, tall, short, wide, long, narrow, lean, round, flat, curved, wavy, ruffled, angular, hollow, tapered, wiry, lopsided, freckled, wrinkled, striped, bright, clear, glossy, jeweled, fiery, shimmering, muddy, drab, dark, grimy, worn, cluttered, fresh, flowery, transparent, sheer, opaque, muscular, handsome, robust, fragile, pale, perky, lacy, shadowy'
    url = 'http://3.13.100.240:8000/api/create_contrast'
    payload = {
        'contrast_type': 'PU',
        'contrast_title': '',
        'model_type': 'english1000',
        'stimuli_type': 'word_list',
        'coordinate_space': 'mni',
        'list1_name': 'sight_words',
        'list1_text': permutedstr,
        # 'colorless, white, ivory1, yellow, gold, olive, green, turquoise, azure, pink, crimson, maroon, lavender, purple, silver, brown, black, mottled, red, ruby, blue, spotted, round, oval, triangular, rectangular, square, shapeless, immense, massive, large, tiny, small, tall, short, wide, long, narrow, lean, round, flat, curved, wavy, ruffled, angular, hollow, tapered, wiry, lopsided, freckled, wrinkled, striped, bright, clear, glossy, jeweled, fiery, shimmering, muddy, drab, dark, grimy, worn, cluttered, fresh, flowery, transparent, sheer, opaque, muscular, handsome, robust, fragile, pale, perky, lacy, shadowy',
        'list2_name': 'touch_words',
        'list2_text': 'lukewarm, mushy, soft, sharp, tepid, oily, woolly, thick, cool, wet, silky, velvety, gritty, icy, spongy, smooth, rough, sandy, cold, slippery, warm, waxy, furry, dry, hot, fleshy, feathery, dull, steamy, rubbery, fuzzy, thin, sticky, bumpy, hairy, fragile, damp, crisp, leathery, tender',
        'csrfmiddlewaretoken': 'xdQAm4JIWKerMYiTEP450VwuM3S3h4nPE5wJvAEoseZ1QpLQ1UgLyEcYUZzhO07W',
        'baseline_choice': False,
        'permutation_choice': False
    }
    # Adding empty header as parameters are being sent in payload
    headers = {
        'X-CSRFToken': 'aC0xfx1Sahs41S7ZE9ux2Xwccq4S6sxBhuGGo3WyGLdE5jAW1eGdAGcGkmL6DohI',
        'Cookie': 'csrftoken=aC0xfx1Sahs41S7ZE9ux2Xwccq4S6sxBhuGGo3WyGLdE5jAW1eGdAGcGkmL6DohI',
    }
    r = requests.post(url, data=json.dumps(payload))
    print(r.content)
    jdata = json.loads(r.content)
    reqlog.write('\n' + jdata['contrast_id'])
    contrastlog.write('\n' + '*'*60)
    contrastlog.write('\n' + jdata['contrast_id'])
    contrastlog.write('\n')
    contrastlog.write(str(payload))
    contrastlog.write('\n' + '*'*60)
    return jdata['contrast_id']


def invokeReq(a, n):
    ls = []
    for i in range(n):
            ls.append(a[i])
    sendRequest(str(ls))

# Generating permutation using Heap Algorithm


def heapPermutation(a, size, n):

        # if size becomes 1 then prints the obtained
        # permutation
    if (size == 1):
        invokeReq(a, n)
        return

    for i in range(size):
        heapPermutation(a, size-1, n)

        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]


if __name__ == "__main__":
    a = list(strs)
    seed = 3
    n = len(a)
    heapPermutation(a, seed, n)
