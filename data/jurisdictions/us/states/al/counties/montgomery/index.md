---
type: Jurisdiction
title: "Montgomery County, AL"
classification: county
fips: "01101"
state: "AL"
demographics:
  population: 225894
  population_under_18: 61859
  population_18_64: 72802
  population_65_plus: 91233
  median_household_income: 61159
  poverty_rate: 20.7
  homeownership_rate: 58.71
  unemployment_rate: 3.44
  median_home_value: 207700
  gini_index: 0.5209
  vacancy_rate: 12.62
  race_white: 64808
  race_black: 133921
  race_asian: 9103
  race_native: 1198
  hispanic: 12002
  bachelors_plus: 79213
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 0.9964
  - to: "us/states/al/districts/senate/25"
    rel: in-district
    area_weight: 0.6332
  - to: "us/states/al/districts/senate/26"
    rel: in-district
    area_weight: 0.3664
  - to: "us/states/al/districts/house/90"
    rel: in-district
    area_weight: 0.3875
  - to: "us/states/al/districts/house/75"
    rel: in-district
    area_weight: 0.2085
  - to: "us/states/al/districts/house/76"
    rel: in-district
    area_weight: 0.1428
  - to: "us/states/al/districts/house/78"
    rel: in-district
    area_weight: 0.1389
  - to: "us/states/al/districts/house/69"
    rel: in-district
    area_weight: 0.0721
  - to: "us/states/al/districts/house/74"
    rel: in-district
    area_weight: 0.0267
  - to: "us/states/al/districts/house/77"
    rel: in-district
    area_weight: 0.0233
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Montgomery County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 225894 |
| Under 18 | 61859 |
| 18–64 | 72802 |
| 65+ | 91233 |
| Median household income | 61159 |
| Poverty rate | 20.7 |
| Homeownership rate | 58.71 |
| Unemployment rate | 3.44 |
| Median home value | 207700 |
| Gini index | 0.5209 |
| Vacancy rate | 12.62 |
| White | 64808 |
| Black | 133921 |
| Asian | 9103 |
| Native | 1198 |
| Hispanic/Latino | 12002 |
| Bachelor's or higher | 79213 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 25](/us/states/al/districts/senate/25.md) — 63% (state senate)
- [AL Senate District 26](/us/states/al/districts/senate/26.md) — 37% (state senate)
- [AL House District 90](/us/states/al/districts/house/90.md) — 39% (state house)
- [AL House District 75](/us/states/al/districts/house/75.md) — 21% (state house)
- [AL House District 76](/us/states/al/districts/house/76.md) — 14% (state house)
- [AL House District 78](/us/states/al/districts/house/78.md) — 14% (state house)
- [AL House District 69](/us/states/al/districts/house/69.md) — 7% (state house)
- [AL House District 74](/us/states/al/districts/house/74.md) — 3% (state house)
- [AL House District 77](/us/states/al/districts/house/77.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
