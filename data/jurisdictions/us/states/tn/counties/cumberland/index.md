---
type: Jurisdiction
title: "Cumberland County, TN"
classification: county
fips: "47035"
state: "TN"
demographics:
  population: 63553
  population_under_18: 11554
  population_18_64: 14781
  population_65_plus: 37218
  median_household_income: 60375
  poverty_rate: 14.35
  homeownership_rate: 80.21
  unemployment_rate: 5.06
  median_home_value: 250500
  gini_index: 0.4314
  vacancy_rate: 10.36
  race_white: 59603
  race_black: 544
  race_asian: 221
  race_native: 49
  hispanic: 2250
  bachelors_plus: 13062
districts:
  - to: "us/states/tn/districts/06"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/tn/districts/senate/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tn/districts/house/25"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Cumberland County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 63553 |
| Under 18 | 11554 |
| 18–64 | 14781 |
| 65+ | 37218 |
| Median household income | 60375 |
| Poverty rate | 14.35 |
| Homeownership rate | 80.21 |
| Unemployment rate | 5.06 |
| Median home value | 250500 |
| Gini index | 0.4314 |
| Vacancy rate | 10.36 |
| White | 59603 |
| Black | 544 |
| Asian | 221 |
| Native | 49 |
| Hispanic/Latino | 2250 |
| Bachelor's or higher | 13062 |

## Districts

- [TN-06](/us/states/tn/districts/06.md) — 100% (congressional)
- [TN Senate District 15](/us/states/tn/districts/senate/15.md) — 100% (state senate)
- [TN House District 25](/us/states/tn/districts/house/25.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
