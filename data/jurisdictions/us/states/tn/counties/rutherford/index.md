---
type: Jurisdiction
title: "Rutherford County, TN"
classification: county
fips: "47149"
state: "TN"
demographics:
  population: 360646
  population_under_18: 89103
  population_18_64: 231245
  population_65_plus: 40298
  median_household_income: 85470
  poverty_rate: 9.27
  homeownership_rate: 64.82
  unemployment_rate: 3.58
  median_home_value: 382600
  gini_index: 0.4021
  vacancy_rate: 6.84
  race_white: 237834
  race_black: 53479
  race_asian: 13222
  race_native: 667
  hispanic: 43964
  bachelors_plus: 109128
districts:
  - to: "us/states/tn/districts/04"
    rel: in-district
    area_weight: 0.992
  - to: "us/states/tn/districts/05"
    rel: in-district
    area_weight: 0.007
  - to: "us/states/tn/districts/senate/13"
    rel: in-district
    area_weight: 0.568
  - to: "us/states/tn/districts/senate/14"
    rel: in-district
    area_weight: 0.4318
  - to: "us/states/tn/districts/house/48"
    rel: in-district
    area_weight: 0.4243
  - to: "us/states/tn/districts/house/13"
    rel: in-district
    area_weight: 0.1948
  - to: "us/states/tn/districts/house/34"
    rel: in-district
    area_weight: 0.162
  - to: "us/states/tn/districts/house/37"
    rel: in-district
    area_weight: 0.1271
  - to: "us/states/tn/districts/house/49"
    rel: in-district
    area_weight: 0.0914
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Rutherford County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 360646 |
| Under 18 | 89103 |
| 18–64 | 231245 |
| 65+ | 40298 |
| Median household income | 85470 |
| Poverty rate | 9.27 |
| Homeownership rate | 64.82 |
| Unemployment rate | 3.58 |
| Median home value | 382600 |
| Gini index | 0.4021 |
| Vacancy rate | 6.84 |
| White | 237834 |
| Black | 53479 |
| Asian | 13222 |
| Native | 667 |
| Hispanic/Latino | 43964 |
| Bachelor's or higher | 109128 |

## Districts

- [TN-04](/us/states/tn/districts/04.md) — 99% (congressional)
- [TN-05](/us/states/tn/districts/05.md) — 1% (congressional)
- [TN Senate District 13](/us/states/tn/districts/senate/13.md) — 57% (state senate)
- [TN Senate District 14](/us/states/tn/districts/senate/14.md) — 43% (state senate)
- [TN House District 48](/us/states/tn/districts/house/48.md) — 42% (state house)
- [TN House District 13](/us/states/tn/districts/house/13.md) — 19% (state house)
- [TN House District 34](/us/states/tn/districts/house/34.md) — 16% (state house)
- [TN House District 37](/us/states/tn/districts/house/37.md) — 13% (state house)
- [TN House District 49](/us/states/tn/districts/house/49.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
