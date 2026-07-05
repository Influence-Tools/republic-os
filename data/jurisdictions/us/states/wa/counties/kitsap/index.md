---
type: Jurisdiction
title: "Kitsap County, WA"
classification: county
fips: "53035"
state: "WA"
demographics:
  population: 277881
  population_under_18: 54706
  population_18_64: 168564
  population_65_plus: 54611
  median_household_income: 104158
  poverty_rate: 8.19
  homeownership_rate: 70.13
  unemployment_rate: 4.67
  median_home_value: 555100
  gini_index: 0.4335
  vacancy_rate: 7.21
  race_white: 208426
  race_black: 6408
  race_asian: 13655
  race_native: 2796
  hispanic: 26018
  bachelors_plus: 103110
districts:
  - to: "us/states/wa/districts/06"
    rel: in-district
    area_weight: 0.7779
  - to: "us/states/wa/districts/senate/23"
    rel: in-district
    area_weight: 0.3117
  - to: "us/states/wa/districts/senate/35"
    rel: in-district
    area_weight: 0.2279
  - to: "us/states/wa/districts/senate/26"
    rel: in-district
    area_weight: 0.1854
  - to: "us/states/wa/districts/house/23"
    rel: in-district
    area_weight: 0.3117
  - to: "us/states/wa/districts/house/35"
    rel: in-district
    area_weight: 0.2279
  - to: "us/states/wa/districts/house/26"
    rel: in-district
    area_weight: 0.1854
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Kitsap County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 277881 |
| Under 18 | 54706 |
| 18–64 | 168564 |
| 65+ | 54611 |
| Median household income | 104158 |
| Poverty rate | 8.19 |
| Homeownership rate | 70.13 |
| Unemployment rate | 4.67 |
| Median home value | 555100 |
| Gini index | 0.4335 |
| Vacancy rate | 7.21 |
| White | 208426 |
| Black | 6408 |
| Asian | 13655 |
| Native | 2796 |
| Hispanic/Latino | 26018 |
| Bachelor's or higher | 103110 |

## Districts

- [WA-06](/us/states/wa/districts/06.md) — 78% (congressional)
- [WA Senate District 23](/us/states/wa/districts/senate/23.md) — 31% (state senate)
- [WA Senate District 35](/us/states/wa/districts/senate/35.md) — 23% (state senate)
- [WA Senate District 26](/us/states/wa/districts/senate/26.md) — 19% (state senate)
- [WA House District 23](/us/states/wa/districts/house/23.md) — 31% (state house)
- [WA House District 35](/us/states/wa/districts/house/35.md) — 23% (state house)
- [WA House District 26](/us/states/wa/districts/house/26.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
