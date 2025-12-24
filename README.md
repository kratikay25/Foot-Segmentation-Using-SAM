# Foot-Segmentation-Using-SAM
Hierarchical foot segmentation using Segment Anything Model (SAM)
FLOWCHART-
Input Image
   ↓
SAM Mask Generation
   ↓
Full Body Mask
   ↓
Lower Body Mask
   ↓
Foot Mask
   ↓
Final Output

Automatic Foot Region Segmentation Using a Hybrid SAM-Based Approach for Diabetic Foot Ulcer Preprocessing

⸻

Abstract

Diabetic Foot Ulcer (DFO) is a serious complication of diabetes that can lead to infection and lower-limb amputation if not detected and monitored at an early stage. Automated analysis of DFO images requires accurate isolation of the foot region as a mandatory preprocessing step. However, foot segmentation in real-world images is challenging due to complex backgrounds, illumination variations, and diverse skin appearances. Traditional image processing techniques often fail under such conditions, while training deep learning models requires large annotated datasets.

This paper presents a hybrid, fully automatic foot region segmentation approach that combines the Segment Anything Model (SAM) with domain-specific rule-based selection and classical morphological refinement. SAM is used as a pretrained foundation segmentation backbone to generate candidate object masks without retraining. These masks are filtered using anatomical, spatial, and skin-color constraints to identify foot regions. Morphological operations and connected component analysis are then applied to refine the segmentation and remove noise. Experimental results on multiple real-world foot images demonstrate that the proposed method effectively isolates the foot region while rejecting background and non-relevant objects, without requiring labeled data or manual interaction. The proposed approach is suitable as a preprocessing stage for DFO analysis systems.

⸻

Keywords

Diabetic Foot Ulcer, Foot Segmentation, Segment Anything Model, Medical Image Preprocessing, Hybrid Segmentation

⸻
1. Introduction

Diabetes mellitus is a chronic metabolic disorder that affects millions of people worldwide. One of its most severe complications is Diabetic Foot Ulcer (DFO), which arises due to neuropathy, poor blood circulation, and delayed wound healing. If not detected and treated in time, DFO can lead to infection and amputation, significantly affecting a patient’s quality of life. Consequently, early monitoring and analysis of foot conditions play a crucial role in diabetic care.

With the increasing availability of medical imaging and mobile health systems, automated image-based analysis has gained attention for assisting clinicians in DFO assessment. A fundamental requirement for such systems is accurate segmentation of the foot region from the input image. Foot region segmentation allows subsequent tasks such as ulcer detection, wound measurement, and tissue classification to be performed more reliably.

However, foot segmentation in real-world images remains a challenging problem. Images captured in clinical or home environments often contain complex backgrounds, shadows, clothing, and varying illumination conditions. Classical image processing techniques such as thresholding, edge detection, and region growing are highly sensitive to these variations and often fail to generalize. Deep learning-based segmentation models can achieve high accuracy but typically require large amounts of labeled data, which is costly and time-consuming to obtain in medical domains.

Recent advances in foundation models have introduced new possibilities for segmentation tasks. The Segment Anything Model (SAM), proposed by Meta AI, is a general-purpose segmentation model capable of generating object masks without task-specific training. While SAM provides robust segmentation proposals, it lacks domain-specific semantic understanding. This paper explores how SAM can be effectively combined with domain-driven rules and classical image processing techniques to achieve reliable foot segmentation without retraining or annotated datasets.

⸻
2. Related Work

Early approaches to foot segmentation relied on classical image processing techniques such as color thresholding, edge detection, and region growing. These methods are computationally efficient but are highly sensitive to illumination changes, skin tone variations, and background clutter. As a result, their performance degrades significantly in real-world scenarios.

Deep learning-based segmentation models, including U-Net, Attention U-Net, and DeepLab variants, have been widely applied to medical image segmentation tasks. These models can learn complex patterns and produce accurate segmentation results when trained with sufficient annotated data. However, their effectiveness depends heavily on the availability of large, well-labeled datasets and their ability to generalize to unseen conditions.

The Segment Anything Model (SAM) represents a new class of foundation models designed for general-purpose segmentation. Unlike task-specific networks, SAM is trained on a massive dataset containing billions of masks and can generate segmentation proposals for arbitrary objects in unseen images. Several recent studies have explored the use of SAM as a backbone for downstream tasks by combining it with additional reasoning or post-processing. However, its application to foot segmentation and DFO preprocessing remains relatively unexplored.

⸻
3. Methodology

The proposed system adopts a hybrid segmentation pipeline that integrates learning-based segmentation with rule-based reasoning and classical image processing. The overall workflow of the proposed approach is illustrated in Figure X.

3.1 Input Image and Preprocessing

The input to the system is a raw RGB image containing bare feet captured under real-world conditions. The image may include background elements such as floor, shadows, and lower leg regions. No manual annotation or cropping is performed.

The input image is first converted from RGB to HSV color space to facilitate skin-color analysis. HSV representation provides better separation of chromatic and intensity information, which is useful for identifying skin-like regions.

3.2 Segment Anything Model (SAM) Mask Generation

The Segment Anything Model is used as a pretrained segmentation backbone. SAM consists of an image encoder, prompt encoder, and mask decoder. In this work, automatic mask generation is employed, which allows SAM to generate multiple candidate object masks without explicit user prompts.

Given an input image, SAM produces a set of segmentation masks corresponding to different objects and regions in the scene. These masks may include feet, legs, background, floor, and other elements. At this stage, SAM does not provide semantic labels or task-specific identification.

3.3 Rule-Based Foot Mask Selection

Since SAM outputs multiple candidate masks, a rule-based selection mechanism is introduced to identify foot regions. Domain-specific knowledge is used to filter masks based on the following criteria:
	•	Skin Color Constraint: Foot regions exhibit skin-like color characteristics in HSV space. Masks with insufficient skin pixel ratio are discarded.
	•	Spatial Constraint: Feet are typically located in the lower-middle portion of the image. Masks whose centroids lie outside this region are rejected.
	•	Shape Constraint: The foot and ankle region exhibits a characteristic height-to-width ratio. Masks that do not satisfy this geometric property are excluded.

By applying these constraints, non-foot regions such as background, floor, and clothing are effectively removed.

3.4 Morphological Refinement

The selected foot mask may still contain small holes or noise due to segmentation imperfections. To address this, classical morphological operations are applied. Morphological closing is used to fill small gaps within the foot region, while opening removes isolated noise pixels.

Connected component analysis is then performed to retain only the largest connected regions corresponding to the left and right feet. This step ensures mask stability and consistency.

3.5 Final Output Generation

The refined binary foot mask is applied to the original RGB image using bitwise masking. The final output is a clean, foot-only segmented image with the background completely removed. This output can be directly used for further DFO analysis tasks.

⸻
4. Experimental Results

The proposed approach was evaluated on multiple real-world foot images captured under varying illumination and background conditions. The evaluation focused on qualitative analysis due to limited availability of ground-truth annotations.

4.1 Intermediate Results

The segmentation process was analyzed at different stages:
	•	SAM Output: Multiple candidate object masks were generated, including feet, background, and floor.
	•	Selected Mask: Rule-based filtering successfully isolated foot regions while rejecting non-relevant objects.
	•	Polished Mask: Morphological refinement produced smooth and noise-free foot masks.
	•	Final Output: Clean foot-only images were obtained with effective background removal.

4.2 Robustness Analysis

The system demonstrated consistent performance across a group of images (GOI) with variations in lighting, pose, and background. Images containing footwear were correctly rejected, indicating appropriate behavior for barefoot-specific applications.

⸻
5. Discussion

The experimental observations highlight several important insights. First, SAM alone is insufficient for domain-specific segmentation tasks due to its lack of semantic understanding. However, when combined with simple rule-based reasoning, it becomes a powerful tool for medical preprocessing. Second, classical image processing techniques remain relevant and effective when used in conjunction with modern deep learning models. The proposed hybrid approach achieves robust segmentation without requiring labeled data or retraining, making it suitable for practical deployment.

⸻
6. Conclusion and Future Work

This paper presented a fully automatic hybrid approach for foot region segmentation using the Segment Anything Model combined with domain-specific rule-based selection and morphological refinement. The proposed method effectively isolates foot regions from complex background images without requiring annotated datasets or manual interaction. The approach is well-suited as a preprocessing stage for Diabetic Foot Ulcer analysis systems.

Future work will focus on integrating ulcer detection and classification modules, extending the approach to video-based analysis, and exploring lightweight task-specific models for real-time deployment.

⸻
References
	1.	Kirillov, A., et al., Segment Anything, ICCV 2023.
	2.	Ronneberger, O., et al., U-Net: Convolutional Networks for Biomedical Image Segmentation, MICCAI 2015.
	3.	Relevant DFO imaging literature (to be added).


