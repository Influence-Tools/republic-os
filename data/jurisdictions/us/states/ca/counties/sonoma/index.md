---
type: Jurisdiction
title: "Sonoma County, CA"
classification: county
fips: "06097"
state: "CA"
demographics:
  population: 485040
  population_under_18: 92397
  population_18_64: 288254
  population_65_plus: 104389
  median_household_income: 104674
  poverty_rate: 8.89
  homeownership_rate: 62.62
  unemployment_rate: 5.71
  median_home_value: 815500
  gini_index: 0.4617
  vacancy_rate: 8.04
  race_white: 299837
  race_black: 7630
  race_asian: 21865
  race_native: 6555
  hispanic: 145518
  bachelors_plus: 188117
districts:
  - to: "us/states/ca/districts/02"
    rel: in-district
    area_weight: 0.7182
  - to: "us/states/ca/districts/04"
    rel: in-district
    area_weight: 0.1811
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.8056
  - to: "us/states/ca/districts/senate/3"
    rel: in-district
    area_weight: 0.0932
  - to: "us/states/ca/districts/house/2"
    rel: in-district
    area_weight: 0.663
  - to: "us/states/ca/districts/house/12"
    rel: in-district
    area_weight: 0.2212
  - to: "us/states/ca/districts/house/4"
    rel: in-district
    area_weight: 0.0147
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Sonoma County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 485040 |
| Under 18 | 92397 |
| 18–64 | 288254 |
| 65+ | 104389 |
| Median household income | 104674 |
| Poverty rate | 8.89 |
| Homeownership rate | 62.62 |
| Unemployment rate | 5.71 |
| Median home value | 815500 |
| Gini index | 0.4617 |
| Vacancy rate | 8.04 |
| White | 299837 |
| Black | 7630 |
| Asian | 21865 |
| Native | 6555 |
| Hispanic/Latino | 145518 |
| Bachelor's or higher | 188117 |

## Districts

- [CA-02](/us/states/ca/districts/02.md) — 72% (congressional)
- [CA-04](/us/states/ca/districts/04.md) — 18% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 81% (state senate)
- [CA Senate District 3](/us/states/ca/districts/senate/3.md) — 9% (state senate)
- [CA House District 2](/us/states/ca/districts/house/2.md) — 66% (state house)
- [CA House District 12](/us/states/ca/districts/house/12.md) — 22% (state house)
- [CA House District 4](/us/states/ca/districts/house/4.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
