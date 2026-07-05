---
type: Jurisdiction
title: "Douglas County, WA"
classification: county
fips: "53017"
state: "WA"
demographics:
  population: 44366
  population_under_18: 10847
  population_18_64: 25339
  population_65_plus: 8180
  median_household_income: 80363
  poverty_rate: 8.26
  homeownership_rate: 69.28
  unemployment_rate: 3.9
  median_home_value: 432500
  gini_index: 0.4313
  vacancy_rate: 11.34
  race_white: 26955
  race_black: 193
  race_asian: 367
  race_native: 501
  hispanic: 15729
  bachelors_plus: 8251
districts:
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/wa/districts/senate/7"
    rel: in-district
    area_weight: 0.9214
  - to: "us/states/wa/districts/senate/13"
    rel: in-district
    area_weight: 0.0786
  - to: "us/states/wa/districts/house/7"
    rel: in-district
    area_weight: 0.9214
  - to: "us/states/wa/districts/house/13"
    rel: in-district
    area_weight: 0.0786
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Douglas County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 44366 |
| Under 18 | 10847 |
| 18–64 | 25339 |
| 65+ | 8180 |
| Median household income | 80363 |
| Poverty rate | 8.26 |
| Homeownership rate | 69.28 |
| Unemployment rate | 3.9 |
| Median home value | 432500 |
| Gini index | 0.4313 |
| Vacancy rate | 11.34 |
| White | 26955 |
| Black | 193 |
| Asian | 367 |
| Native | 501 |
| Hispanic/Latino | 15729 |
| Bachelor's or higher | 8251 |

## Districts

- [WA-04](/us/states/wa/districts/04.md) — 100% (congressional)
- [WA Senate District 7](/us/states/wa/districts/senate/7.md) — 92% (state senate)
- [WA Senate District 13](/us/states/wa/districts/senate/13.md) — 8% (state senate)
- [WA House District 7](/us/states/wa/districts/house/7.md) — 92% (state house)
- [WA House District 13](/us/states/wa/districts/house/13.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
