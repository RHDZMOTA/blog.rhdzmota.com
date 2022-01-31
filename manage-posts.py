import os
import json
import fire
import datetime as dt
import logging
from typing import Dict, List, Tuple, Optional

import yaml


logger = logging.getLogger(__name__)


SITE_BLOGPOST_CONFIGS_PATH = os.environ.get(
    "SITE_BLOGPOST_CONFIGS_PATH",
    default="blogpost-configs"
)


SITE_BLOGPOST_TARGET_PATH = os.environ.get(
    "SITE_BLOGPOST_TARGET_PATH",
    default=os.path.join("content", "post")
)

SITE_BLOGPOST_CONTENT_PATH = os.environ.get(
    "SITE_BLOGPOST_CONTENT_PATH",
    default="public-notes"
)


class Main:

    def __init__(self):
        self.start = dt.datetime.utcnow()

    def ignore_list(
            self,
            overwrite_blogpost_configs_path: Optional[str] = None,
    ) -> List[str]:
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        ignore_filepath = os.path.join(blogpost_configs_path, "ignore.yaml")
        with open(ignore_filepath, "r") as file:
            content = file.read()
        return yaml.safe_load(content)

    def list_configs(
            self,
            overwrite_blogpost_configs_path: Optional[str] = None,
    ) -> List[str]:
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        return [
            filename
            for filename in os.listdir(blogpost_configs_path)
            if filename.endswith(".json")
        ]

    def list_hackmd(
            self,
            overwrite_blogpost_content_path: Optional[str] = None,
            overwrite_blogpost_configs_path: Optional[str] = None,
            ignore: bool = False
    ):
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        blogpost_content_path = overwrite_blogpost_content_path or SITE_BLOGPOST_CONTENT_PATH
        ignore_list = self.ignore_list(overwrite_blogpost_configs_path=blogpost_configs_path) \
            if ignore else []
        return [
            filename
            for filename in os.listdir(blogpost_content_path)
            if (filename not in ignore_list) and filename.endswith(".md")
        ]

    def get_config(
            self,
            config_name: str,
            overwrite_blogpost_configs_path: Optional[str] = None
    ) -> Dict:
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        filename = config_name if config_name.endswith(".json") else f"{config_name}.json"
        filepath = os.path.join(blogpost_configs_path, filename)
        with open(filepath, "r") as file:
            content = file.read()
        return json.loads(content)

    def get_index_content(
            self,
            config_name: str,
            overwrite_blogpost_content_path: Optional[str] = None,
            overwrite_blogpost_configs_path: Optional[str] = None
    ):
        # Optional arguments
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        blogpost_content_path = overwrite_blogpost_content_path or SITE_BLOGPOST_CONTENT_PATH
        # Infer post name from config name
        post_name, _ = os.path.splitext(config_name)
        post_path = os.path.join(blogpost_content_path, f"{post_name}.md")
        if not os.path.exists(post_path):
            raise ValueError(f"Content post path not found: {post_path}")
        # Get config
        config = self.get_config(
            config_name=config_name,
            overwrite_blogpost_configs_path=overwrite_blogpost_configs_path
        )
        # Add/parse configs
        config["tags"] = "\n- ".join(config.get("tags", []))
        config["categories"] = repr(config.get("categories", []))
        config["created_at"] = dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        config["content_path"] = os.path.join(blogpost_content_path, f"{post_name}.md")
        # Load template
        template_path = os.path.join(blogpost_configs_path, "_template.txt")
        with open(template_path, "r") as file:
            content = file.read()
        # Return parsed tempalte
        return content.format(
            **config
        )

    def create_post(
            self,
            post_name: str,
            overwrite_blogpost_target_path: Optional[str] = None,
            overwrite_blogpost_content_path: Optional[str] = None,
            overwrite_blogpost_configs_path: Optional[str] = None,
    ):
        post_name, _ = os.path.splitext(post_name)
        # Optional arguments
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        blogpost_content_path = overwrite_blogpost_content_path or SITE_BLOGPOST_CONTENT_PATH
        blogpost_target_path = overwrite_blogpost_target_path or SITE_BLOGPOST_TARGET_PATH
        # Get index content
        index_content = self.get_index_content(
            config_name=post_name,
            overwrite_blogpost_configs_path=blogpost_configs_path,
            overwrite_blogpost_content_path=blogpost_content_path,
        )
        # Create output target path
        output_path = os.path.join(blogpost_target_path, post_name)
        os.makedirs(output_path, exist_ok=True)
        # Create index
        index_filepath = os.path.join(output_path, "index.md")
        with open(index_filepath, "w") as file:
            file.write(index_content)

    def create_posts(
            self,
            overwrite_blogpost_target_path: Optional[str] = None,
            overwrite_blogpost_content_path: Optional[str] = None,
            overwrite_blogpost_configs_path: Optional[str] = None,
    ):
        # Optional arguments
        blogpost_configs_path = overwrite_blogpost_configs_path or SITE_BLOGPOST_CONFIGS_PATH
        blogpost_content_path = overwrite_blogpost_content_path or SITE_BLOGPOST_CONTENT_PATH
        blogpost_target_path = overwrite_blogpost_target_path or SITE_BLOGPOST_TARGET_PATH
        # Get config list
        config_list = self.list_configs(
            overwrite_blogpost_configs_path=overwrite_blogpost_configs_path
        )
        # Create post
        errors = []
        successes = []
        for config in config_list:
            try:
                logger.warn(f"Working on post config: {config}")
                self.create_post(
                    post_name=config,
                    overwrite_blogpost_target_path=blogpost_target_path,
                    overwrite_blogpost_configs_path=blogpost_configs_path,
                    overwrite_blogpost_content_path=blogpost_content_path,
                )
                successes.append(config)
            except Exception as e:
                logger.error(e)
                errors.append(config)
        return {
            "errors": errors,
            "successes": successes
        }


if __name__ == "__main__":
    fire.Fire(Main())
