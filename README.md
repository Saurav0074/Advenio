## Segmenting the given image into three different regions

Firstly,  an initial look-up on the image made it clear that the Optic Disk class, the atrophy class and the background class are all touching each other and hence, the traditional thresholding and contour detection methods would be unable to treat them distinctly.

A second thought was the marker-based image segmentation using Watershed algorithm which is considered to be very useful in such cases because of its implicit assumption of the image surface being composed of peaks and valleys where high intensity denotes peaks and hills while low intensity denotes valleys; we start by filling water (color) in the valleys and making barriers in order to prevent the merging of peaks with valleys; these barriers eventually form the border-line of segmentation.


You can use the [editor on GitHub](https://github.com/Saurav0074/Advenio/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Saurav0074/Advenio/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
