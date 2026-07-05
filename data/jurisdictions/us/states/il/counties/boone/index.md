---
type: Jurisdiction
title: "Boone County, IL"
classification: county
fips: "17007"
state: "IL"
demographics:
  population: 53230
  population_under_18: 12650
  population_18_64: 31664
  population_65_plus: 8916
  median_household_income: 84571
  poverty_rate: 9.93
  homeownership_rate: 81.78
  unemployment_rate: 7.36
  median_home_value: 216900
  gini_index: 0.4217
  vacancy_rate: 4.1
  race_white: 38201
  race_black: 1623
  race_asian: 511
  race_native: 194
  hispanic: 13651
  bachelors_plus: 11785
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.6699
  - to: "us/states/il/districts/11"
    rel: in-district
    area_weight: 0.3301
  - to: "us/states/il/districts/senate/35"
    rel: in-district
    area_weight: 0.5049
  - to: "us/states/il/districts/senate/45"
    rel: in-district
    area_weight: 0.4325
  - to: "us/states/il/districts/senate/34"
    rel: in-district
    area_weight: 0.0625
  - to: "us/states/il/districts/house/69"
    rel: in-district
    area_weight: 0.5049
  - to: "us/states/il/districts/house/89"
    rel: in-district
    area_weight: 0.2486
  - to: "us/states/il/districts/house/90"
    rel: in-district
    area_weight: 0.1839
  - to: "us/states/il/districts/house/68"
    rel: in-district
    area_weight: 0.0625
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Boone County, IL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53230 |
| Under 18 | 12650 |
| 18–64 | 31664 |
| 65+ | 8916 |
| Median household income | 84571 |
| Poverty rate | 9.93 |
| Homeownership rate | 81.78 |
| Unemployment rate | 7.36 |
| Median home value | 216900 |
| Gini index | 0.4217 |
| Vacancy rate | 4.1 |
| White | 38201 |
| Black | 1623 |
| Asian | 511 |
| Native | 194 |
| Hispanic/Latino | 13651 |
| Bachelor's or higher | 11785 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 67% (congressional)
- [IL-11](/us/states/il/districts/11.md) — 33% (congressional)
- [IL Senate District 35](/us/states/il/districts/senate/35.md) — 50% (state senate)
- [IL Senate District 45](/us/states/il/districts/senate/45.md) — 43% (state senate)
- [IL Senate District 34](/us/states/il/districts/senate/34.md) — 6% (state senate)
- [IL House District 69](/us/states/il/districts/house/69.md) — 50% (state house)
- [IL House District 89](/us/states/il/districts/house/89.md) — 25% (state house)
- [IL House District 90](/us/states/il/districts/house/90.md) — 18% (state house)
- [IL House District 68](/us/states/il/districts/house/68.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
