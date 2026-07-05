---
type: Jurisdiction
title: "George County, MS"
classification: county
fips: "28039"
state: "MS"
demographics:
  population: 25170
  population_under_18: 6699
  population_18_64: 14726
  population_65_plus: 3745
  median_household_income: 59758
  poverty_rate: 18.29
  homeownership_rate: 82.11
  unemployment_rate: 7.46
  median_home_value: 166900
  gini_index: 0.4474
  vacancy_rate: 10.32
  race_white: 21696
  race_black: 1811
  race_asian: 33
  race_native: 28
  hispanic: 786
  bachelors_plus: 3691
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ms/districts/senate/43"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/house/107"
    rel: in-district
    area_weight: 0.6901
  - to: "us/states/ms/districts/house/109"
    rel: in-district
    area_weight: 0.1779
  - to: "us/states/ms/districts/house/105"
    rel: in-district
    area_weight: 0.132
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# George County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25170 |
| Under 18 | 6699 |
| 18–64 | 14726 |
| 65+ | 3745 |
| Median household income | 59758 |
| Poverty rate | 18.29 |
| Homeownership rate | 82.11 |
| Unemployment rate | 7.46 |
| Median home value | 166900 |
| Gini index | 0.4474 |
| Vacancy rate | 10.32 |
| White | 21696 |
| Black | 1811 |
| Asian | 33 |
| Native | 28 |
| Hispanic/Latino | 786 |
| Bachelor's or higher | 3691 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 100% (congressional)
- [MS Senate District 43](/us/states/ms/districts/senate/43.md) — 100% (state senate)
- [MS House District 107](/us/states/ms/districts/house/107.md) — 69% (state house)
- [MS House District 109](/us/states/ms/districts/house/109.md) — 18% (state house)
- [MS House District 105](/us/states/ms/districts/house/105.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
