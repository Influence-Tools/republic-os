---
type: Jurisdiction
title: "San Luis Obispo County, CA"
classification: county
fips: "06079"
state: "CA"
demographics:
  population: 281555
  population_under_18: 49244
  population_18_64: 169973
  population_65_plus: 62338
  median_household_income: 97446
  poverty_rate: 12.91
  homeownership_rate: 62.09
  unemployment_rate: 5.48
  median_home_value: 824700
  gini_index: 0.4749
  vacancy_rate: 12.86
  race_white: 195251
  race_black: 3267
  race_asian: 10471
  race_native: 2632
  hispanic: 70318
  bachelors_plus: 105623
districts:
  - to: "us/states/ca/districts/24"
    rel: in-district
    area_weight: 0.5546
  - to: "us/states/ca/districts/19"
    rel: in-district
    area_weight: 0.3641
  - to: "us/states/ca/districts/senate/17"
    rel: in-district
    area_weight: 0.541
  - to: "us/states/ca/districts/senate/21"
    rel: in-district
    area_weight: 0.3779
  - to: "us/states/ca/districts/house/30"
    rel: in-district
    area_weight: 0.8998
  - to: "us/states/ca/districts/house/37"
    rel: in-district
    area_weight: 0.019
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# San Luis Obispo County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 281555 |
| Under 18 | 49244 |
| 18–64 | 169973 |
| 65+ | 62338 |
| Median household income | 97446 |
| Poverty rate | 12.91 |
| Homeownership rate | 62.09 |
| Unemployment rate | 5.48 |
| Median home value | 824700 |
| Gini index | 0.4749 |
| Vacancy rate | 12.86 |
| White | 195251 |
| Black | 3267 |
| Asian | 10471 |
| Native | 2632 |
| Hispanic/Latino | 70318 |
| Bachelor's or higher | 105623 |

## Districts

- [CA-24](/us/states/ca/districts/24.md) — 55% (congressional)
- [CA-19](/us/states/ca/districts/19.md) — 36% (congressional)
- [CA Senate District 17](/us/states/ca/districts/senate/17.md) — 54% (state senate)
- [CA Senate District 21](/us/states/ca/districts/senate/21.md) — 38% (state senate)
- [CA House District 30](/us/states/ca/districts/house/30.md) — 90% (state house)
- [CA House District 37](/us/states/ca/districts/house/37.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
