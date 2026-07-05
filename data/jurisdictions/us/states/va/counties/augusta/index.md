---
type: Jurisdiction
title: "Augusta County, VA"
classification: county
fips: "51015"
state: "VA"
demographics:
  population: 78033
  population_under_18: 14340
  population_18_64: 46067
  population_65_plus: 17626
  median_household_income: 82049
  poverty_rate: 6.64
  homeownership_rate: 80.19
  unemployment_rate: 2.42
  median_home_value: 306100
  gini_index: 0.416
  vacancy_rate: 6.12
  race_white: 69697
  race_black: 3339
  race_asian: 345
  race_native: 93
  hispanic: 3132
  bachelors_plus: 19539
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/va/districts/senate/2"
    rel: in-district
    area_weight: 0.7582
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.2417
  - to: "us/states/va/districts/house/35"
    rel: in-district
    area_weight: 0.7582
  - to: "us/states/va/districts/house/36"
    rel: in-district
    area_weight: 0.2417
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Augusta County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 78033 |
| Under 18 | 14340 |
| 18–64 | 46067 |
| 65+ | 17626 |
| Median household income | 82049 |
| Poverty rate | 6.64 |
| Homeownership rate | 80.19 |
| Unemployment rate | 2.42 |
| Median home value | 306100 |
| Gini index | 0.416 |
| Vacancy rate | 6.12 |
| White | 69697 |
| Black | 3339 |
| Asian | 345 |
| Native | 93 |
| Hispanic/Latino | 3132 |
| Bachelor's or higher | 19539 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 2](/us/states/va/districts/senate/2.md) — 76% (state senate)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 24% (state senate)
- [VA House District 35](/us/states/va/districts/house/35.md) — 76% (state house)
- [VA House District 36](/us/states/va/districts/house/36.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
