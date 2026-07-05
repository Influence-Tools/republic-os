---
type: Jurisdiction
title: "St. Landry Parish, LA"
classification: county
fips: "22097"
state: "LA"
demographics:
  population: 81670
  population_under_18: 21689
  population_18_64: 46140
  population_65_plus: 13841
  median_household_income: 44462
  poverty_rate: 26.76
  homeownership_rate: 70.07
  unemployment_rate: 6.34
  median_home_value: 142500
  gini_index: 0.4943
  vacancy_rate: 13.55
  race_white: 42790
  race_black: 32754
  race_asian: 473
  race_native: 81
  hispanic: 2510
  bachelors_plus: 10656
districts:
  - to: "us/states/la/districts/06"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.7383
  - to: "us/states/la/districts/senate/24"
    rel: in-district
    area_weight: 0.243
  - to: "us/states/la/districts/senate/28"
    rel: in-district
    area_weight: 0.0187
  - to: "us/states/la/districts/house/46"
    rel: in-district
    area_weight: 0.4534
  - to: "us/states/la/districts/house/28"
    rel: in-district
    area_weight: 0.2117
  - to: "us/states/la/districts/house/40"
    rel: in-district
    area_weight: 0.2113
  - to: "us/states/la/districts/house/41"
    rel: in-district
    area_weight: 0.1234
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# St. Landry Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 81670 |
| Under 18 | 21689 |
| 18–64 | 46140 |
| 65+ | 13841 |
| Median household income | 44462 |
| Poverty rate | 26.76 |
| Homeownership rate | 70.07 |
| Unemployment rate | 6.34 |
| Median home value | 142500 |
| Gini index | 0.4943 |
| Vacancy rate | 13.55 |
| White | 42790 |
| Black | 32754 |
| Asian | 473 |
| Native | 81 |
| Hispanic/Latino | 2510 |
| Bachelor's or higher | 10656 |

## Districts

- [LA-06](/us/states/la/districts/06.md) — 100% (congressional)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 74% (state senate)
- [LA Senate District 24](/us/states/la/districts/senate/24.md) — 24% (state senate)
- [LA Senate District 28](/us/states/la/districts/senate/28.md) — 2% (state senate)
- [LA House District 46](/us/states/la/districts/house/46.md) — 45% (state house)
- [LA House District 28](/us/states/la/districts/house/28.md) — 21% (state house)
- [LA House District 40](/us/states/la/districts/house/40.md) — 21% (state house)
- [LA House District 41](/us/states/la/districts/house/41.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
