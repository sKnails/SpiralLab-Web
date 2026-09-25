from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PhotoFisherSiteTests(unittest.TestCase):
    def read(self, name: str) -> str:
        return (ROOT / name).read_text(encoding="utf-8")

    def test_static_site_has_required_public_files(self):
        for name in ("index.html", "privacy.html", "styles.css", "404.html", "README.md"):
            with self.subTest(name=name):
                self.assertTrue((ROOT / name).is_file())

    def test_homepage_explains_product_and_links_privacy(self):
        page = self.read("index.html")

        for phrase in (
            "Photo Fisher",
            "photo and video navigator",
            "camera roll",
            "How it works",
            "Privacy-first",
            "Support",
            "privacy.html",
            "Google Play",
            "App Store",
            "Coming soon",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, page)

    def test_privacy_page_covers_v1_data_practices(self):
        page = self.read("privacy.html").lower()

        for phrase in (
            "permission",
            "camera roll",
            "no account",
            "no backend",
            "no uploads",
            "no analytics",
            "no advertising sdk",
            "not sell",
            "other apps",
            "system share",
            "google play",
            "app store",
            "privacy@kuhtey.com",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, page)

    def test_readme_marks_launch_details_as_required_before_release(self):
        readme = self.read("README.md").lower()

        for phrase in (
            "privacy@kuhtey.com",
            "alias",
            "legal publisher",
            "store urls",
            "ad/analytics disclosures",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, readme)

    def test_custom_domain_is_not_enabled_yet(self):
        self.assertFalse((ROOT / "CNAME").exists())


if __name__ == "__main__":
    unittest.main()
