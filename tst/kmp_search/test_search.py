from src.kmp_search.search import KMPSearch


def test_create_lps_table() -> None:
    assert [0, 0, 0, 0, 0, 0, 1, 2, 3] == KMPSearch.create_lps_table(
        pattern="catdogcat"
    )
    assert [0, 0, 0, 0, 0, 0, 1, 2, 3, 0] == KMPSearch.create_lps_table(
        pattern="catdogcata"
    )
    assert [0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 2, 3] == KMPSearch.create_lps_table(
        pattern="catdogcatcat"
    )
    assert [0, 0, 0, 0, 0, 0, 0, 0] == KMPSearch.create_lps_table(pattern="squirrel")


def test_kmp_search() -> None:
    text = "aaacatdogcatxxx"
    assert [3, 9] == KMPSearch("cat").search(text)
    assert [3] == KMPSearch("catdogcat").search(text)
    assert [3] == KMPSearch("catdogcatxxx").search(text)
    assert [0] == KMPSearch("aaa").search(text)
    assert [] == KMPSearch("squirrel").search(text)
    text = "aaacatdogcabbbcatdogcataaa"
    assert [14] == KMPSearch("catdogcat").search(text)
