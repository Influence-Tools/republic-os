---
type: Jurisdiction
title: "Albemarle County, VA"
classification: county
fips: "51003"
state: "VA"
demographics:
  population: 114919
  population_under_18: 22438
  population_18_64: 69012
  population_65_plus: 23469
  median_household_income: 104392
  poverty_rate: 7.67
  homeownership_rate: 65.93
  unemployment_rate: 3.4
  median_home_value: 495400
  gini_index: 0.4759
  vacancy_rate: 6.61
  race_white: 85958
  race_black: 10584
  race_asian: 6680
  race_native: 399
  hispanic: 8647
  bachelors_plus: 73129
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.9865
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.0123
  - to: "us/states/va/districts/senate/11"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/55"
    rel: in-district
    area_weight: 0.9718
  - to: "us/states/va/districts/house/54"
    rel: in-district
    area_weight: 0.0281
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Albemarle County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 114919 |
| Under 18 | 22438 |
| 18–64 | 69012 |
| 65+ | 23469 |
| Median household income | 104392 |
| Poverty rate | 7.67 |
| Homeownership rate | 65.93 |
| Unemployment rate | 3.4 |
| Median home value | 495400 |
| Gini index | 0.4759 |
| Vacancy rate | 6.61 |
| White | 85958 |
| Black | 10584 |
| Asian | 6680 |
| Native | 399 |
| Hispanic/Latino | 8647 |
| Bachelor's or higher | 73129 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 99% (congressional)
- [VA-07](/us/states/va/districts/07.md) — 1% (congressional)
- [VA Senate District 11](/us/states/va/districts/senate/11.md) — 100% (state senate)
- [VA House District 55](/us/states/va/districts/house/55.md) — 97% (state house)
- [VA House District 54](/us/states/va/districts/house/54.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
