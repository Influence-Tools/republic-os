---
type: Jurisdiction
title: "Franklin city, VA"
classification: county
fips: "51620"
state: "VA"
demographics:
  population: 8250
  population_under_18: 2355
  population_18_64: 2414
  population_65_plus: 3481
  median_household_income: 63245
  poverty_rate: 19.35
  homeownership_rate: 53.88
  unemployment_rate: 7.93
  median_home_value: 256600
  gini_index: 0.4259
  vacancy_rate: 11.66
  race_white: 3141
  race_black: 4601
  race_asian: 3
  race_native: 0
  hispanic: 261
  bachelors_plus: 2118
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/84"
    rel: in-district
    area_weight: 0.9982
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Franklin city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8250 |
| Under 18 | 2355 |
| 18–64 | 2414 |
| 65+ | 3481 |
| Median household income | 63245 |
| Poverty rate | 19.35 |
| Homeownership rate | 53.88 |
| Unemployment rate | 7.93 |
| Median home value | 256600 |
| Gini index | 0.4259 |
| Vacancy rate | 11.66 |
| White | 3141 |
| Black | 4601 |
| Asian | 3 |
| Native | 0 |
| Hispanic/Latino | 261 |
| Bachelor's or higher | 2118 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 100% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 100% (state senate)
- [VA House District 84](/us/states/va/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
