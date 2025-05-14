import json
import pandas
class Product:
    def __init__(self, product_id, reviews=[], product_name="", stats = {}):
        self.product_id = product_id
        self.reviews = reviews
        self.product_name = product_name
        self.stats = stats
    def __str__(self):
        return f"""product_id: {self.product_id}
           product_name: {self.product_name}
           stats: {json.dumps(self.stats, indent=4, ensure_ascii=False)}
           reviews: {"\n\n".join(str(review) for review in self.reviews)}
        """
    def reviews_to_dict(self):
        return [review.to_dict() for review in self.reviews]

    def info_to_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "stats": self.stats
        }

    def extract_name(self):
        pass

    def extract_reviews(self):
        pass

    def calculate_stats(self):
        reviews = pandas.DataFrame


        reviews_count = reviews.shape[0]
        pros_count = reviews.pros.astype(bool).sum()
        cons_count = reviews.cons.astype(bool).sum()
        pros_cons_count = reviews.apply(lambda r: bool(r.pros) and bool(r.cons), axis=1).sum()
        average_stars = round(reviews.stars.mean(),2)