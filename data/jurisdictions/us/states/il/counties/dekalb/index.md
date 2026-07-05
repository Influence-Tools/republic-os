---
type: Jurisdiction
title: "DeKalb County, IL"
classification: county
fips: "17037"
state: "IL"
demographics:
  population: 100703
  population_under_18: 21723
  population_18_64: 64960
  population_65_plus: 14020
  median_household_income: 70724
  poverty_rate: 14.8
  homeownership_rate: 61.39
  unemployment_rate: 6.8
  median_home_value: 243600
  gini_index: 0.45
  vacancy_rate: 5.11
  race_white: 74678
  race_black: 7056
  race_asian: 2331
  race_native: 658
  hispanic: 14647
  bachelors_plus: 28035
districts:
  - to: "us/states/il/districts/14"
    rel: in-district
    area_weight: 0.699
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.1664
  - to: "us/states/il/districts/11"
    rel: in-district
    area_weight: 0.1346
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.3233
  - to: "us/states/il/districts/senate/45"
    rel: in-district
    area_weight: 0.2814
  - to: "us/states/il/districts/senate/35"
    rel: in-district
    area_weight: 0.2493
  - to: "us/states/il/districts/senate/38"
    rel: in-district
    area_weight: 0.146
  - to: "us/states/il/districts/house/74"
    rel: in-district
    area_weight: 0.3233
  - to: "us/states/il/districts/house/89"
    rel: in-district
    area_weight: 0.2814
  - to: "us/states/il/districts/house/70"
    rel: in-district
    area_weight: 0.2493
  - to: "us/states/il/districts/house/76"
    rel: in-district
    area_weight: 0.1202
  - to: "us/states/il/districts/house/75"
    rel: in-district
    area_weight: 0.0258
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# DeKalb County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 100703 |
| Under 18 | 21723 |
| 18–64 | 64960 |
| 65+ | 14020 |
| Median household income | 70724 |
| Poverty rate | 14.8 |
| Homeownership rate | 61.39 |
| Unemployment rate | 6.8 |
| Median home value | 243600 |
| Gini index | 0.45 |
| Vacancy rate | 5.11 |
| White | 74678 |
| Black | 7056 |
| Asian | 2331 |
| Native | 658 |
| Hispanic/Latino | 14647 |
| Bachelor's or higher | 28035 |

## Districts

- [IL-14](/us/states/il/districts/14.md) — 70% (congressional)
- [IL-16](/us/states/il/districts/16.md) — 17% (congressional)
- [IL-11](/us/states/il/districts/11.md) — 13% (congressional)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 32% (state senate)
- [IL Senate District 45](/us/states/il/districts/senate/45.md) — 28% (state senate)
- [IL Senate District 35](/us/states/il/districts/senate/35.md) — 25% (state senate)
- [IL Senate District 38](/us/states/il/districts/senate/38.md) — 15% (state senate)
- [IL House District 74](/us/states/il/districts/house/74.md) — 32% (state house)
- [IL House District 89](/us/states/il/districts/house/89.md) — 28% (state house)
- [IL House District 70](/us/states/il/districts/house/70.md) — 25% (state house)
- [IL House District 76](/us/states/il/districts/house/76.md) — 12% (state house)
- [IL House District 75](/us/states/il/districts/house/75.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
