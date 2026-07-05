---
type: Jurisdiction
title: "Crawford County, KS"
classification: county
fips: "20037"
state: "KS"
demographics:
  population: 39008
  population_under_18: 8662
  population_18_64: 24123
  population_65_plus: 6223
  median_household_income: 52844
  poverty_rate: 20.61
  homeownership_rate: 60.79
  unemployment_rate: 4.07
  median_home_value: 132600
  gini_index: 0.4643
  vacancy_rate: 12.62
  race_white: 33844
  race_black: 681
  race_asian: 655
  race_native: 206
  hispanic: 2936
  bachelors_plus: 10209
districts:
  - to: "us/states/ks/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/2"
    rel: in-district
    area_weight: 0.8846
  - to: "us/states/ks/districts/house/3"
    rel: in-district
    area_weight: 0.1153
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Crawford County, KS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39008 |
| Under 18 | 8662 |
| 18–64 | 24123 |
| 65+ | 6223 |
| Median household income | 52844 |
| Poverty rate | 20.61 |
| Homeownership rate | 60.79 |
| Unemployment rate | 4.07 |
| Median home value | 132600 |
| Gini index | 0.4643 |
| Vacancy rate | 12.62 |
| White | 33844 |
| Black | 681 |
| Asian | 655 |
| Native | 206 |
| Hispanic/Latino | 2936 |
| Bachelor's or higher | 10209 |

## Districts

- [KS-02](/us/states/ks/districts/02.md) — 100% (congressional)
- [KS Senate District 13](/us/states/ks/districts/senate/13.md) — 100% (state senate)
- [KS House District 2](/us/states/ks/districts/house/2.md) — 88% (state house)
- [KS House District 3](/us/states/ks/districts/house/3.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
