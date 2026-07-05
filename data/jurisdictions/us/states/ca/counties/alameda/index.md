---
type: Jurisdiction
title: "Alameda County, CA"
classification: county
fips: "06001"
state: "CA"
demographics:
  population: 1649473
  population_under_18: 326276
  population_18_64: 1069036
  population_65_plus: 254161
  median_household_income: 129367
  poverty_rate: 9.22
  homeownership_rate: 54.41
  unemployment_rate: 5.38
  median_home_value: 1090100
  gini_index: 0.4765
  vacancy_rate: 6.12
  race_white: 492184
  race_black: 158576
  race_asian: 543240
  race_native: 16403
  hispanic: 386114
  bachelors_plus: 902516
districts:
  - to: "us/states/ca/districts/14"
    rel: in-district
    area_weight: 0.7149
  - to: "us/states/ca/districts/12"
    rel: in-district
    area_weight: 0.1172
  - to: "us/states/ca/districts/17"
    rel: in-district
    area_weight: 0.0656
  - to: "us/states/ca/districts/10"
    rel: in-district
    area_weight: 0.0141
  - to: "us/states/ca/districts/senate/5"
    rel: in-district
    area_weight: 0.5098
  - to: "us/states/ca/districts/senate/10"
    rel: in-district
    area_weight: 0.2092
  - to: "us/states/ca/districts/senate/7"
    rel: in-district
    area_weight: 0.105
  - to: "us/states/ca/districts/senate/9"
    rel: in-district
    area_weight: 0.0896
  - to: "us/states/ca/districts/house/16"
    rel: in-district
    area_weight: 0.4757
  - to: "us/states/ca/districts/house/20"
    rel: in-district
    area_weight: 0.169
  - to: "us/states/ca/districts/house/24"
    rel: in-district
    area_weight: 0.1489
  - to: "us/states/ca/districts/house/18"
    rel: in-district
    area_weight: 0.0896
  - to: "us/states/ca/districts/house/14"
    rel: in-district
    area_weight: 0.0302
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Alameda County, CA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1649473 |
| Under 18 | 326276 |
| 18–64 | 1069036 |
| 65+ | 254161 |
| Median household income | 129367 |
| Poverty rate | 9.22 |
| Homeownership rate | 54.41 |
| Unemployment rate | 5.38 |
| Median home value | 1090100 |
| Gini index | 0.4765 |
| Vacancy rate | 6.12 |
| White | 492184 |
| Black | 158576 |
| Asian | 543240 |
| Native | 16403 |
| Hispanic/Latino | 386114 |
| Bachelor's or higher | 902516 |

## Districts

- [CA-14](/us/states/ca/districts/14.md) — 71% (congressional)
- [CA-12](/us/states/ca/districts/12.md) — 12% (congressional)
- [CA-17](/us/states/ca/districts/17.md) — 7% (congressional)
- [CA-10](/us/states/ca/districts/10.md) — 1% (congressional)
- [CA Senate District 5](/us/states/ca/districts/senate/5.md) — 51% (state senate)
- [CA Senate District 10](/us/states/ca/districts/senate/10.md) — 21% (state senate)
- [CA Senate District 7](/us/states/ca/districts/senate/7.md) — 10% (state senate)
- [CA Senate District 9](/us/states/ca/districts/senate/9.md) — 9% (state senate)
- [CA House District 16](/us/states/ca/districts/house/16.md) — 48% (state house)
- [CA House District 20](/us/states/ca/districts/house/20.md) — 17% (state house)
- [CA House District 24](/us/states/ca/districts/house/24.md) — 15% (state house)
- [CA House District 18](/us/states/ca/districts/house/18.md) — 9% (state house)
- [CA House District 14](/us/states/ca/districts/house/14.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
