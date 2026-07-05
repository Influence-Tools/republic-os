---
type: Jurisdiction
title: "Jefferson County, WI"
classification: county
fips: "55055"
state: "WI"
demographics:
  population: 86003
  population_under_18: 16971
  population_18_64: 53099
  population_65_plus: 15933
  median_household_income: 83750
  poverty_rate: 8.11
  homeownership_rate: 73.13
  unemployment_rate: 3.55
  median_home_value: 274100
  gini_index: 0.4025
  vacancy_rate: 5.47
  race_white: 76167
  race_black: 809
  race_asian: 561
  race_native: 362
  hispanic: 7309
  bachelors_plus: 22502
districts:
  - to: "us/states/wi/districts/05"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/wi/districts/senate/16"
    rel: in-district
    area_weight: 0.3863
  - to: "us/states/wi/districts/senate/33"
    rel: in-district
    area_weight: 0.3002
  - to: "us/states/wi/districts/senate/13"
    rel: in-district
    area_weight: 0.2699
  - to: "us/states/wi/districts/senate/15"
    rel: in-district
    area_weight: 0.0436
  - to: "us/states/wi/districts/house/46"
    rel: in-district
    area_weight: 0.3863
  - to: "us/states/wi/districts/house/38"
    rel: in-district
    area_weight: 0.2699
  - to: "us/states/wi/districts/house/97"
    rel: in-district
    area_weight: 0.2374
  - to: "us/states/wi/districts/house/99"
    rel: in-district
    area_weight: 0.0628
  - to: "us/states/wi/districts/house/43"
    rel: in-district
    area_weight: 0.0436
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Jefferson County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 86003 |
| Under 18 | 16971 |
| 18–64 | 53099 |
| 65+ | 15933 |
| Median household income | 83750 |
| Poverty rate | 8.11 |
| Homeownership rate | 73.13 |
| Unemployment rate | 3.55 |
| Median home value | 274100 |
| Gini index | 0.4025 |
| Vacancy rate | 5.47 |
| White | 76167 |
| Black | 809 |
| Asian | 561 |
| Native | 362 |
| Hispanic/Latino | 7309 |
| Bachelor's or higher | 22502 |

## Districts

- [WI-05](/us/states/wi/districts/05.md) — 100% (congressional)
- [WI Senate District 16](/us/states/wi/districts/senate/16.md) — 39% (state senate)
- [WI Senate District 33](/us/states/wi/districts/senate/33.md) — 30% (state senate)
- [WI Senate District 13](/us/states/wi/districts/senate/13.md) — 27% (state senate)
- [WI Senate District 15](/us/states/wi/districts/senate/15.md) — 4% (state senate)
- [WI House District 46](/us/states/wi/districts/house/46.md) — 39% (state house)
- [WI House District 38](/us/states/wi/districts/house/38.md) — 27% (state house)
- [WI House District 97](/us/states/wi/districts/house/97.md) — 24% (state house)
- [WI House District 99](/us/states/wi/districts/house/99.md) — 6% (state house)
- [WI House District 43](/us/states/wi/districts/house/43.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
