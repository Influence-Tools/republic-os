---
type: Jurisdiction
title: "Johnson County, IN"
classification: county
fips: "18081"
state: "IN"
demographics:
  population: 166315
  population_under_18: 40361
  population_18_64: 99769
  population_65_plus: 26185
  median_household_income: 90454
  poverty_rate: 7.44
  homeownership_rate: 72.73
  unemployment_rate: 3.0
  median_home_value: 284600
  gini_index: 0.4246
  vacancy_rate: 5.1
  race_white: 140778
  race_black: 5461
  race_asian: 8542
  race_native: 806
  hispanic: 7159
  bachelors_plus: 54213
districts:
  - to: "us/states/in/districts/06"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/in/districts/senate/41"
    rel: in-district
    area_weight: 0.4622
  - to: "us/states/in/districts/senate/37"
    rel: in-district
    area_weight: 0.3552
  - to: "us/states/in/districts/senate/32"
    rel: in-district
    area_weight: 0.1537
  - to: "us/states/in/districts/senate/36"
    rel: in-district
    area_weight: 0.0289
  - to: "us/states/in/districts/house/47"
    rel: in-district
    area_weight: 0.669
  - to: "us/states/in/districts/house/58"
    rel: in-district
    area_weight: 0.2198
  - to: "us/states/in/districts/house/60"
    rel: in-district
    area_weight: 0.0591
  - to: "us/states/in/districts/house/57"
    rel: in-district
    area_weight: 0.0521
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Johnson County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 166315 |
| Under 18 | 40361 |
| 18–64 | 99769 |
| 65+ | 26185 |
| Median household income | 90454 |
| Poverty rate | 7.44 |
| Homeownership rate | 72.73 |
| Unemployment rate | 3.0 |
| Median home value | 284600 |
| Gini index | 0.4246 |
| Vacancy rate | 5.1 |
| White | 140778 |
| Black | 5461 |
| Asian | 8542 |
| Native | 806 |
| Hispanic/Latino | 7159 |
| Bachelor's or higher | 54213 |

## Districts

- [IN-06](/us/states/in/districts/06.md) — 100% (congressional)
- [IN Senate District 41](/us/states/in/districts/senate/41.md) — 46% (state senate)
- [IN Senate District 37](/us/states/in/districts/senate/37.md) — 36% (state senate)
- [IN Senate District 32](/us/states/in/districts/senate/32.md) — 15% (state senate)
- [IN Senate District 36](/us/states/in/districts/senate/36.md) — 3% (state senate)
- [IN House District 47](/us/states/in/districts/house/47.md) — 67% (state house)
- [IN House District 58](/us/states/in/districts/house/58.md) — 22% (state house)
- [IN House District 60](/us/states/in/districts/house/60.md) — 6% (state house)
- [IN House District 57](/us/states/in/districts/house/57.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
