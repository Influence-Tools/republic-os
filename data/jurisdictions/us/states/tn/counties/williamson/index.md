---
type: Jurisdiction
title: "Williamson County, TN"
classification: county
fips: "47187"
state: "TN"
demographics:
  population: 260351
  population_under_18: 67203
  population_18_64: 154744
  population_65_plus: 38404
  median_household_income: 135594
  poverty_rate: 4.64
  homeownership_rate: 78.81
  unemployment_rate: 2.43
  median_home_value: 751900
  gini_index: 0.4505
  vacancy_rate: 4.86
  race_white: 213322
  race_black: 10189
  race_asian: 13977
  race_native: 595
  hispanic: 15611
  bachelors_plus: 149131
districts:
  - to: "us/states/tn/districts/05"
    rel: in-district
    area_weight: 0.5311
  - to: "us/states/tn/districts/07"
    rel: in-district
    area_weight: 0.4664
  - to: "us/states/tn/districts/senate/27"
    rel: in-district
    area_weight: 0.9836
  - to: "us/states/tn/districts/senate/28"
    rel: in-district
    area_weight: 0.0162
  - to: "us/states/tn/districts/house/65"
    rel: in-district
    area_weight: 0.4695
  - to: "us/states/tn/districts/house/63"
    rel: in-district
    area_weight: 0.2967
  - to: "us/states/tn/districts/house/61"
    rel: in-district
    area_weight: 0.1535
  - to: "us/states/tn/districts/house/92"
    rel: in-district
    area_weight: 0.0801
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Williamson County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 260351 |
| Under 18 | 67203 |
| 18–64 | 154744 |
| 65+ | 38404 |
| Median household income | 135594 |
| Poverty rate | 4.64 |
| Homeownership rate | 78.81 |
| Unemployment rate | 2.43 |
| Median home value | 751900 |
| Gini index | 0.4505 |
| Vacancy rate | 4.86 |
| White | 213322 |
| Black | 10189 |
| Asian | 13977 |
| Native | 595 |
| Hispanic/Latino | 15611 |
| Bachelor's or higher | 149131 |

## Districts

- [TN-05](/us/states/tn/districts/05.md) — 53% (congressional)
- [TN-07](/us/states/tn/districts/07.md) — 47% (congressional)
- [TN Senate District 27](/us/states/tn/districts/senate/27.md) — 98% (state senate)
- [TN Senate District 28](/us/states/tn/districts/senate/28.md) — 2% (state senate)
- [TN House District 65](/us/states/tn/districts/house/65.md) — 47% (state house)
- [TN House District 63](/us/states/tn/districts/house/63.md) — 30% (state house)
- [TN House District 61](/us/states/tn/districts/house/61.md) — 15% (state house)
- [TN House District 92](/us/states/tn/districts/house/92.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
