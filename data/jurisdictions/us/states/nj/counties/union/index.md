---
type: Jurisdiction
title: "Union County, NJ"
classification: county
fips: "34039"
state: "NJ"
demographics:
  population: 579290
  population_under_18: 136260
  population_18_64: 355753
  population_65_plus: 87277
  median_household_income: 103202
  poverty_rate: 9.18
  homeownership_rate: 57.36
  unemployment_rate: 6.51
  median_home_value: 529200
  gini_index: 0.4834
  vacancy_rate: 4.29
  race_white: 228008
  race_black: 115397
  race_asian: 32637
  race_native: 3233
  hispanic: 203905
  bachelors_plus: 215946
districts:
  - to: "us/states/nj/districts/07"
    rel: in-district
    area_weight: 0.561
  - to: "us/states/nj/districts/10"
    rel: in-district
    area_weight: 0.2478
  - to: "us/states/nj/districts/08"
    rel: in-district
    area_weight: 0.1284
  - to: "us/states/nj/districts/12"
    rel: in-district
    area_weight: 0.0569
  - to: "us/states/nj/districts/senate/22"
    rel: in-district
    area_weight: 0.4005
  - to: "us/states/nj/districts/senate/21"
    rel: in-district
    area_weight: 0.3096
  - to: "us/states/nj/districts/senate/20"
    rel: in-district
    area_weight: 0.2508
  - to: "us/states/nj/districts/senate/28"
    rel: in-district
    area_weight: 0.0265
  - to: "us/states/nj/districts/house/22"
    rel: in-district
    area_weight: 0.4005
  - to: "us/states/nj/districts/house/21"
    rel: in-district
    area_weight: 0.3096
  - to: "us/states/nj/districts/house/20"
    rel: in-district
    area_weight: 0.2508
  - to: "us/states/nj/districts/house/28"
    rel: in-district
    area_weight: 0.0265
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Union County, NJ

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 579290 |
| Under 18 | 136260 |
| 18–64 | 355753 |
| 65+ | 87277 |
| Median household income | 103202 |
| Poverty rate | 9.18 |
| Homeownership rate | 57.36 |
| Unemployment rate | 6.51 |
| Median home value | 529200 |
| Gini index | 0.4834 |
| Vacancy rate | 4.29 |
| White | 228008 |
| Black | 115397 |
| Asian | 32637 |
| Native | 3233 |
| Hispanic/Latino | 203905 |
| Bachelor's or higher | 215946 |

## Districts

- [NJ-07](/us/states/nj/districts/07.md) — 56% (congressional)
- [NJ-10](/us/states/nj/districts/10.md) — 25% (congressional)
- [NJ-08](/us/states/nj/districts/08.md) — 13% (congressional)
- [NJ-12](/us/states/nj/districts/12.md) — 6% (congressional)
- [NJ Senate District 22](/us/states/nj/districts/senate/22.md) — 40% (state senate)
- [NJ Senate District 21](/us/states/nj/districts/senate/21.md) — 31% (state senate)
- [NJ Senate District 20](/us/states/nj/districts/senate/20.md) — 25% (state senate)
- [NJ Senate District 28](/us/states/nj/districts/senate/28.md) — 3% (state senate)
- [NJ House District 22](/us/states/nj/districts/house/22.md) — 40% (state house)
- [NJ House District 21](/us/states/nj/districts/house/21.md) — 31% (state house)
- [NJ House District 20](/us/states/nj/districts/house/20.md) — 25% (state house)
- [NJ House District 28](/us/states/nj/districts/house/28.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
