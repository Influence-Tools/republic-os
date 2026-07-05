---
type: Jurisdiction
title: "Black Hawk County, IA"
classification: county
fips: "19013"
state: "IA"
demographics:
  population: 131049
  population_under_18: 28744
  population_18_64: 79167
  population_65_plus: 23138
  median_household_income: 66417
  poverty_rate: 14.95
  homeownership_rate: 66.23
  unemployment_rate: 4.56
  median_home_value: 188900
  gini_index: 0.4494
  vacancy_rate: 7.51
  race_white: 104148
  race_black: 12135
  race_asian: 3565
  race_native: 382
  hispanic: 6861
  bachelors_plus: 34410
districts:
  - to: "us/states/ia/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/34"
    rel: in-district
    area_weight: 0.3564
  - to: "us/states/ia/districts/senate/38"
    rel: in-district
    area_weight: 0.3543
  - to: "us/states/ia/districts/senate/27"
    rel: in-district
    area_weight: 0.1927
  - to: "us/states/ia/districts/house/68"
    rel: in-district
    area_weight: 0.3563
  - to: "us/states/ia/districts/house/76"
    rel: in-district
    area_weight: 0.3188
  - to: "us/states/ia/districts/house/54"
    rel: in-district
    area_weight: 0.1927
  - to: "us/states/ia/districts/house/62"
    rel: in-district
    area_weight: 0.0561
  - to: "us/states/ia/districts/house/61"
    rel: in-district
    area_weight: 0.0405
  - to: "us/states/ia/districts/house/75"
    rel: in-district
    area_weight: 0.0355
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Black Hawk County, IA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 131049 |
| Under 18 | 28744 |
| 18–64 | 79167 |
| 65+ | 23138 |
| Median household income | 66417 |
| Poverty rate | 14.95 |
| Homeownership rate | 66.23 |
| Unemployment rate | 4.56 |
| Median home value | 188900 |
| Gini index | 0.4494 |
| Vacancy rate | 7.51 |
| White | 104148 |
| Black | 12135 |
| Asian | 3565 |
| Native | 382 |
| Hispanic/Latino | 6861 |
| Bachelor's or higher | 34410 |

## Districts

- [IA-02](/us/states/ia/districts/02.md) — 100% (congressional)
- [IA Senate District 34](/us/states/ia/districts/senate/34.md) — 36% (state senate)
- [IA Senate District 38](/us/states/ia/districts/senate/38.md) — 35% (state senate)
- [IA Senate District 27](/us/states/ia/districts/senate/27.md) — 19% (state senate)
- [IA House District 68](/us/states/ia/districts/house/68.md) — 36% (state house)
- [IA House District 76](/us/states/ia/districts/house/76.md) — 32% (state house)
- [IA House District 54](/us/states/ia/districts/house/54.md) — 19% (state house)
- [IA House District 62](/us/states/ia/districts/house/62.md) — 6% (state house)
- [IA House District 61](/us/states/ia/districts/house/61.md) — 4% (state house)
- [IA House District 75](/us/states/ia/districts/house/75.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
